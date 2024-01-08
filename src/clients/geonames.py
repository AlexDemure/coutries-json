import re
from io import BytesIO
from typing import Any
from typing import Optional
from zipfile import ZipFile

import requests
from bs4 import BeautifulSoup

from src.core.settings import Settings
from src.utils import check_dir
from src.utils import check_file
from src.utils import string_to_csv
from src.utils import tuple_to_dict
from src.utils import txtf
from src.utils import zipf


class _GeonamesClient:
    download_url: str = None
    dir: str = None
    filename: Optional[str] = None

    @classmethod
    def download(cls, filename: Optional[str] = None) -> None:
        if not filename:
            filename = cls.filename

        filepath = f"{cls.dir}/{txtf(filename)}"

        print(f"[Geonames] Start download file {filepath}")

        check_dir(cls.dir)

        if check_file(filepath):
            print(f"[Geonames] Already exists file {filepath}")
            return

        response = requests.get(f"{cls.download_url}/{zipf(filename)}")

        archive = ZipFile(BytesIO(response.content))

        with open(filepath, "w") as file:
            file.write(archive.read(txtf(filename)).decode())

        print(f"[Geonames] Finish download file {filepath}")

    @classmethod
    def read(cls, filename: str) -> list[tuple]:
        with open(f"{cls.dir}/{txtf(filename)}") as file:
            rows = string_to_csv(file.read())
        return rows

    @classmethod
    def get(cls, *args, **kwargs) -> Any:
        raise NotImplementedError


class GeonamesCity(_GeonamesClient):
    download_url: str = "https://download.geonames.org/export/dump"

    dir = f"{Settings.STATIC_DIR}/{Settings.GEONAMES_DIR}"

    filename = "cities15000"

    @classmethod
    def get(cls, filename: str) -> list[dict]:
        """
        The main 'geoname' table has the following fields :
        ---------------------------------------------------
        geonameid         : integer id of record in geonames database
        name              : name of geographical point (utf8) varchar(200)
        asciiname         : name of geographical point in plain ascii characters, varchar(200)
        alternatenames    : alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table, varchar(10000)
        latitude          : latitude in decimal degrees (wgs84)
        longitude         : longitude in decimal degrees (wgs84)
        feature class     : see http://www.geonames.org/export/codes.html, char(1)
        feature code      : see http://www.geonames.org/export/codes.html, varchar(10)
        country code      : ISO-3166 2-letter country code, 2 characters
        cc2               : alternate country codes, comma separated, ISO-3166 2-letter country code, 200 characters
        admin1 code       : fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; varchar(20)
        admin2 code       : code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80)
        admin3 code       : code for third level administrative division, varchar(20)
        admin4 code       : code for fourth level administrative division, varchar(20)
        population        : bigint (8 byte int)
        elevation         : in meters, integer
        dem               : digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
        timezone          : the iana timezone id (see file timeZone.txt) varchar(40)
        modification date : date of last modification in yyyy-MM-dd format
        """

        rows = cls.read(filename)

        rows = [
            tuple_to_dict(Settings.SQLITE_GEONAMES_CITY_KEYS, row)
            for row in rows
            if row
        ]

        rows = [
            row
            for row in rows
            if int(row["population"]) >= Settings.GEONAMES_MIN_POPULATION
            and row["feature_code"] in Settings.GEONAMES_FEATURE_CODES
        ]

        if rows:
            print(f"[Geonames] Cities found for {filename}: {len(rows)}")
        else:
            print(f"[Geonames] Cities not found for {filename}")

        return rows


class GeonamesAlternate(_GeonamesClient):
    download_url: str = "https://download.geonames.org/export/dump/alternatenames"

    dir: str = f"{Settings.STATIC_DIR}/{Settings.GEONAMES_DIR}/alternatenames"

    @classmethod
    def filenames(cls) -> list[str]:
        response = requests.get(cls.download_url)

        countries = [
            tag.string.split(".zip")[0]
            for tag in BeautifulSoup(response.text, "html.parser").findAll("a")
            if re.findall(".zip", tag.text)
        ]

        return countries

    @classmethod
    def get(cls, filename: str, city_ids: list[int]) -> list[dict]:
        """
        The table 'alternate names' :
        -----------------------------
        alternateNameId   : the id of this alternate name, int
        geonameid         : geonameId referring to id in table 'geoname', int
        isolanguage       : iso 639 language code 2- or 3-characters, optionally followed by a hyphen and a countrycode for country specific variants (ex:zh-CN) or by a variant name (ex: zh-Hant); 4-characters 'post' for postal codes and 'iata','icao' and faac for airport codes, fr_1793 for French Revolution names,  abbr for abbreviation, link to a website (mostly to wikipedia), wkdt for the wikidataid, varchar(7)
        alternate name    : alternate name or name variant, varchar(400)
        isPreferredName   : '1', if this alternate name is an official/preferred name
        isShortName       : '1', if this is a short name like 'California' for 'State of California'
        isColloquial      : '1', if this alternate name is a colloquial or slang term. Example: 'Big Apple' for 'New York'.
        isHistoric        : '1', if this alternate name is historic and was used in the past. Example 'Bombay' for 'Mumbai'.
        from		  : from period when the name was used
        to		  : to period when the name was used

        Remark : the field 'alternatenames' in the table 'geoname' is a short version of the 'alternatenames' table without links and postal codes but with ascii transliterations. You probably don't need both.
        If you don't need to know the language of a name variant, the field 'alternatenames' will be sufficient. If you need to know the language
        of a name variant, then you will need to load the table 'alternatenames' and you can drop the column in the geoname table.
        """

        def rules(_row: dict):
            if not _row["language_id"]:  # Если не указан язык альтернативного названия
                return False

            if (
                _row["language_id"] not in Settings.AVAILABLE_LANGUAGES
            ):  # Если не указан язык из тех что мы собираем.
                return False

            if _row["is_colloquial"]:  # Не сленг
                return False

            if _row["is_historic"]:  # Не историческая
                return False

            if re.findall(r"(?i)city", _row["alternate_name"]):  # Нет в названии City
                return False

            return True

        rows = cls.read(filename)

        rows = [
            row for row in rows if row and int(row[1]) in city_ids
        ]  # Только записи которые подходят по городам

        rows = [
            tuple_to_dict(Settings.SQLITE_GEONAMES_ALTER_KEYS, row)
            for row in rows
            if row
        ]

        rows = [row for row in rows if rules(row)]

        if rows:
            print(f"[Geonames] Alternates found for {filename}: {len(rows)}")
        else:
            print(f"[Geonames] Alternates not found for {filename}: {city_ids}")

        return rows

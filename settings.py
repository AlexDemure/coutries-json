from dataclasses import dataclass

# GEONAMES_CITIES_FILENAME_TXT: str = "cities15000.txt"
# GEONAMES_CITIES_FILENAME_ZIP: str = "cities15000.zip"
# GEONAMES_DOWNLOAD_URL: str = "https://download.geonames.org/export/dump"
# PROXY_FREE_LIST_HOST: str = "https://www.sslproxies.org/"


@dataclass
class LanguageSettings:
    AVAILABLE_LANGUAGES: list[str] = ('en', 'ru')


@dataclass
class SQLiteSettings:
    SQLITE_DATABASE: str = 'countries.db'
    SQLITE_GEONAMES_CITY_TABLE: str = "geo_cities"
    SQLITE_GEONAMES_CITY_KEYS: list[str] = (
        "id",
        "name",
        "asciiname",
        "alternatenames",
        "latitude",
        "longitude",
        "feature_class",
        "feature_code",
        "country_id",
        "cc2",
        "admin1_code",
        "admin2_code",
        "admin3_code",
        "admin4_code",
        "population",
        "elevation",
        "dem",
        "timezone",
    )
    SQLITE_GEONAMES_ALTER_TABLE: str = "geo_alters"
    SQLITE_GEONAMES_ALTER_KEYS: list[str] = (
        "id",
        "city_id",
        "language_id",
        "alternate_name",
        "is_preferred_name",
        "is_short_name",
        "is_colloquial",
        "is_historic",
    )
    SQLITE_CITY_TABLE: str = "cities"
    SQLITE_CITY_KEYS: list[str] = (
        "id",
        "country_id",
        "origin",
        "ascii",
        "en",
        "ru",
    )
    SQLITE_COUNTRY_TABLE: str = "countries"
    SQLITE_COUNTRY_KEYS: list[str] = (
        "id",
        "iso",
        "en",
        "ru",
    )

    SQLITE_LANGUAGE_TABLE: str = "languages"
    SQLITE_LANGUAGE_KEYS: list[str] = (
        "id",
        "origin",
        "name"
    )


@dataclass
class GeonamesSettings:
    GEONAMES_DIR: str = "geonames"

    GEONAMES_MIN_POPULATION: int = 500000  # Мин. количество населения в городе
    GEONAMES_FEATURE_CODES: list[str] = (  # Тип. населенного пункта
        'PPLC',
        'PPLA',
        'PPLA2',
        'PPLA3',
        'PPLA4',
        'PPLA5'
    )


@dataclass
class ProxySettings:
    PROXY_HOSTS: list[str] = (
        "****:8000",
    )
    PROXY_USERNAME: str = "****"
    PROXY_PASSWORD: str = "****"


configs = [LanguageSettings, SQLiteSettings, GeonamesSettings, ProxySettings]


@dataclass
class Settings(*configs):
    STATIC_DIR = 'static'

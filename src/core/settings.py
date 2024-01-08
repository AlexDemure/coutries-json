from dataclasses import dataclass


@dataclass
class LanguageSettings:
    AVAILABLE_LANGUAGES: list[str] = ("en", "de")


@dataclass
class SQLiteSettings:
    SQLITE_DATABASE: str = "countries.db"
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
        *[language for language in LanguageSettings.AVAILABLE_LANGUAGES],
    )
    SQLITE_COUNTRY_TABLE: str = "countries"
    SQLITE_COUNTRY_KEYS: list[str] = (
        "id",
        *[language for language in LanguageSettings.AVAILABLE_LANGUAGES],
    )

    SQLITE_LANGUAGE_TABLE: str = "languages"
    SQLITE_LANGUAGE_KEYS: list[str] = ("id", "origin", "name")

    SQLITE_M2M_COUNTRY_LANGUAGE_TABLE: str = "country_languages"
    SQLITE_M2M_COUNTRY_LANGUAGE_KEYS: list[str] = ("id", "country_id", "language_id")


@dataclass
class GeonamesSettings:
    GEONAMES_DIR: str = "geonames"

    GEONAMES_MIN_POPULATION: int = 1000000  # Мин. количество населения в городе
    GEONAMES_FEATURE_CODES: list[str] = (  # Тип. населенного пункта
        "PPLC",
        "PPLA",
        "PPLA2",
        "PPLA3",
        "PPLA4",
        "PPLA5",
    )


@dataclass
class StefangabosSettings:
    STEFANGABOS_DIR: str = "stefangabos"


@dataclass
class GitHubSettings:
    GITHUB_DIR: str = "github"


@dataclass
class StoreSettings:
    STORE_DIR: str = "stores"


@dataclass
class ProxySettings:
    PROXY: bool = False
    PROXY_HOSTS: list[str] = (
        "188.130.201.52:8000",
        "188.130.201.191:8000",
        "188.130.202.21:8000",
    )
    PROXY_USERNAME: str = "VLMHbX"
    PROXY_PASSWORD: str = "FbJeb5"


configs = [
    LanguageSettings,
    SQLiteSettings,
    GeonamesSettings,
    StefangabosSettings,
    GitHubSettings,
    StoreSettings,
    ProxySettings,
]


@dataclass
class Settings(*configs):
    STATIC_DIR = "src/static"
    RETURN_FILENAME = "countries"

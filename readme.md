# Customizable options
| Name                                               | Default      | Comment                                                                                |   |   |
|----------------------------------------------------|--------------|----------------------------------------------------------------------------------------|---|---|
| AVAILABLE_LANGUAGES                                | ("en", "de") | Countries and cities in the selected language                                          |   |   |
| GEONAMES_MIN_POPULATION                            | 1 000 000    | Collection of cities with a population of more than                                    |   |   |
| PROXY, PROXY_HOSTS, PROXY_USERNAME, PROXY_PASSWORD | False        | Proxy server for OpenStreetMap (rate api limit 0.6 sec.) https://proxy6.net/user/proxy |   |   |

# Depends:
- bs4
- requests
- unidecode

# Run
```
pc:~/coutries-json$: python3 cli.py
```

# Static:
- https://download.geonames.org/export/dump/
- https://stefangabos.github.io/world_countries/
- Github & Web pages (Mix)

# Files:
- countries.db - SQLite3
- countries.json


# countries.json
```
[
    {
        "id": "af",
        "en": "Afghanistan",
        "de": "Afghanistan",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1138958,
                "country_id": "af",
                "origin": "Kabul",
                "ascii": "Kabul",
                "en": "Kabul",
                "de": "Kabul"
            }
        ]
    },
    {
        "id": "al",
        "en": "Albania",
        "de": "Albanien",
        "languages": [
            {
                "id": "sq",
                "origin": "Shqip",
                "name": "Albanian"
            }
        ],
        "cities": []
    },
    {
        "id": "dz",
        "en": "Algeria",
        "de": "Algerien",
        "languages": [
            {
                "id": "ar",
                "origin": "العربية",
                "name": "Arabic"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2507480,
                "country_id": "dz",
                "origin": "Algiers",
                "ascii": "Algiers",
                "en": "Algiers",
                "de": "Algier"
            }
        ]
    },
    {
        "id": "ad",
        "en": "Andorra",
        "de": "Andorra",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "ao",
        "en": "Angola",
        "de": "Angola",
        "languages": [
            {
                "id": "ao",
                "origin": null,
                "name": "Portuguese (Angola)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2240449,
                "country_id": "ao",
                "origin": "Luanda",
                "ascii": "Luanda",
                "en": "Luanda",
                "de": "Luanda"
            }
        ]
    },
    {
        "id": "ag",
        "en": "Antigua and barbuda",
        "de": "Antigua und barbuda",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "ar",
        "en": "Argentina",
        "de": "Argentinien",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3435910,
                "country_id": "ar",
                "origin": "Buenos Aires",
                "ascii": "Buenos Aires",
                "en": "Buenos Aires",
                "de": "Buenos Aires"
            },
            {
                "id": 3860259,
                "country_id": "ar",
                "origin": "Córdoba",
                "ascii": "Cordoba",
                "en": "Cordoba",
                "de": "Córdoba"
            }
        ]
    },
    {
        "id": "am",
        "en": "Armenia",
        "de": "Armenien",
        "languages": [
            {
                "id": "hy",
                "origin": "Հայերեն",
                "name": "Armenian"
            }
        ],
        "cities": [
            {
                "id": 616052,
                "country_id": "am",
                "origin": "Yerevan",
                "ascii": "Yerevan",
                "en": "Yerevan",
                "de": "Jerewan"
            }
        ]
    },
    {
        "id": "au",
        "en": "Australia",
        "de": "Australien",
        "languages": [
            {
                "id": "au",
                "origin": null,
                "name": "English (Australia)"
            }
        ],
        "cities": [
            {
                "id": 2063523,
                "country_id": "au",
                "origin": "Perth",
                "ascii": "Perth",
                "en": "Perth",
                "de": "Perth"
            },
            {
                "id": 2078025,
                "country_id": "au",
                "origin": "Adelaide",
                "ascii": "Adelaide",
                "en": "Adelaide",
                "de": "Adelaide"
            },
            {
                "id": 2147714,
                "country_id": "au",
                "origin": "Sydney",
                "ascii": "Sydney",
                "en": "Sydney",
                "de": "Sydney"
            },
            {
                "id": 2158177,
                "country_id": "au",
                "origin": "Melbourne",
                "ascii": "Melbourne",
                "en": "Melbourne",
                "de": "Melbourne"
            },
            {
                "id": 2174003,
                "country_id": "au",
                "origin": "Brisbane",
                "ascii": "Brisbane",
                "en": "Brisbane",
                "de": "Brisbane"
            }
        ]
    },
    {
        "id": "at",
        "en": "Austria",
        "de": "Österreich",
        "languages": [
            {
                "id": "de",
                "origin": "Deutsch",
                "name": "German"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2761369,
                "country_id": "at",
                "origin": "Vienna",
                "ascii": "Vienna",
                "en": "Vienna",
                "de": "Wien"
            }
        ]
    },
    {
        "id": "az",
        "en": "Azerbaijan",
        "de": "Aserbaidschan",
        "languages": [
            {
                "id": "az",
                "origin": "azərbaycan dili",
                "name": "Azerbaijani"
            }
        ],
        "cities": [
            {
                "id": 587084,
                "country_id": "az",
                "origin": "Baku",
                "ascii": "Baku",
                "en": "Baku",
                "de": "Baku"
            }
        ]
    },
    {
        "id": "bs",
        "en": "Bahamas",
        "de": "Bahamas",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "bh",
        "en": "Bahrain",
        "de": "Bahrain",
        "languages": [
            {
                "id": "ar",
                "origin": "العربية",
                "name": "Arabic"
            }
        ],
        "cities": []
    },
    {
        "id": "bd",
        "en": "Bangladesh",
        "de": "Bangladesch",
        "languages": [
            {
                "id": "bn",
                "origin": "বাংলা",
                "name": "Bengali"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1185188,
                "country_id": "bd",
                "origin": "Rangpur",
                "ascii": "Rangpur",
                "en": "Rangpur",
                "de": "Rangpur"
            },
            {
                "id": 1185241,
                "country_id": "bd",
                "origin": "Dhaka",
                "ascii": "Dhaka",
                "en": "Dhaka",
                "de": "Dhaka"
            },
            {
                "id": 1205733,
                "country_id": "bd",
                "origin": "Chattogram",
                "ascii": "Chattogram",
                "en": "Chittagong",
                "de": "Chittagong"
            },
            {
                "id": 1336135,
                "country_id": "bd",
                "origin": "Khulna",
                "ascii": "Khulna",
                "en": "Khulna",
                "de": "Khulna"
            }
        ]
    },
    {
        "id": "bb",
        "en": "Barbados",
        "de": "Barbados",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "by",
        "en": "Belarus",
        "de": "Belarus",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 625144,
                "country_id": "by",
                "origin": "Minsk",
                "ascii": "Minsk",
                "en": "Minsk",
                "de": "Minsk"
            }
        ]
    },
    {
        "id": "be",
        "en": "Belgium",
        "de": "Belgien",
        "languages": [
            {
                "id": "nl",
                "origin": "Nederlands, Vlaams",
                "name": "Dutch"
            },
            {
                "id": "fr",
                "origin": "français, langue française",
                "name": "French"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2800866,
                "country_id": "be",
                "origin": "Brussels",
                "ascii": "Brussels",
                "en": "Brussels",
                "de": "Brüssel"
            }
        ]
    },
    {
        "id": "bz",
        "en": "Belize",
        "de": "Belize",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "bj",
        "en": "Benin",
        "de": "Benin",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "bt",
        "en": "Bhutan",
        "de": "Bhutan",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "bo",
        "en": "Bolivia (plurinational state of)",
        "de": "Bolivien",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3904906,
                "country_id": "bo",
                "origin": "Santa Cruz de la Sierra",
                "ascii": "Santa Cruz de la Sierra",
                "en": "Santa Cruz de la Sierra",
                "de": "Santa Cruz de la Sierra"
            }
        ]
    },
    {
        "id": "ba",
        "en": "Bosnia and herzegovina",
        "de": "Bosnien und herzegowina",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            },
            {
                "id": "hr",
                "origin": "hrvatski",
                "name": "Croatian"
            }
        ],
        "cities": []
    },
    {
        "id": "bw",
        "en": "Botswana",
        "de": "Botswana",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "br",
        "en": "Brazil",
        "de": "Brasilien",
        "languages": [
            {
                "id": "br",
                "origin": "brezhoneg",
                "name": "Portuguese (Brazil)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3390760,
                "country_id": "br",
                "origin": "Recife",
                "ascii": "Recife",
                "en": "Recife",
                "de": "Recife"
            },
            {
                "id": 3395981,
                "country_id": "br",
                "origin": "Maceió",
                "ascii": "Maceio",
                "en": "Maceio",
                "de": "Maceió"
            },
            {
                "id": 3399415,
                "country_id": "br",
                "origin": "Fortaleza",
                "ascii": "Fortaleza",
                "en": "Fortaleza",
                "de": "Fortaleza"
            },
            {
                "id": 3405870,
                "country_id": "br",
                "origin": "Belém",
                "ascii": "Belem",
                "en": "Belem",
                "de": "Belém"
            },
            {
                "id": 3448439,
                "country_id": "br",
                "origin": "São Paulo",
                "ascii": "Sao Paulo",
                "en": "Sao Paulo",
                "de": "São Paulo"
            },
            {
                "id": 3450554,
                "country_id": "br",
                "origin": "Salvador",
                "ascii": "Salvador",
                "en": "Salvador",
                "de": "Salvador da Bahia"
            },
            {
                "id": 3451190,
                "country_id": "br",
                "origin": "Rio de Janeiro",
                "ascii": "Rio de Janeiro",
                "en": "Rio de Janeiro",
                "de": "Rio de Janeiro"
            },
            {
                "id": 3452925,
                "country_id": "br",
                "origin": "Porto Alegre",
                "ascii": "Porto Alegre",
                "en": "Porto Alegre",
                "de": "Porto Alegre"
            },
            {
                "id": 3462377,
                "country_id": "br",
                "origin": "Goiânia",
                "ascii": "Goiania",
                "en": "Goiania",
                "de": "Goiânia"
            },
            {
                "id": 3464975,
                "country_id": "br",
                "origin": "Curitiba",
                "ascii": "Curitiba",
                "en": "Curitiba",
                "de": "Curitiba"
            },
            {
                "id": 3469058,
                "country_id": "br",
                "origin": "Brasília",
                "ascii": "Brasilia",
                "en": "Brasilia",
                "de": "Brasília"
            },
            {
                "id": 3470127,
                "country_id": "br",
                "origin": "Belo Horizonte",
                "ascii": "Belo Horizonte",
                "en": "Belo Horizonte",
                "de": "Belo Horizonte"
            },
            {
                "id": 3663517,
                "country_id": "br",
                "origin": "Manaus",
                "ascii": "Manaus",
                "en": "Manaus",
                "de": "Manaus"
            }
        ]
    },
    {
        "id": "bn",
        "en": "Brunei darussalam",
        "de": "Brunei",
        "languages": [
            {
                "id": "ms",
                "origin": "bahasa Melayu, بهاس ملايو‎",
                "name": "Malay"
            }
        ],
        "cities": []
    },
    {
        "id": "bg",
        "en": "Bulgaria",
        "de": "Bulgarien",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 727011,
                "country_id": "bg",
                "origin": "Sofia",
                "ascii": "Sofia",
                "en": "Sofia",
                "de": "Sofia"
            }
        ]
    },
    {
        "id": "bf",
        "en": "Burkina faso",
        "de": "Burkina faso",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2357048,
                "country_id": "bf",
                "origin": "Ouagadougou",
                "ascii": "Ouagadougou",
                "en": "Ouagadougou",
                "de": "Ouagadougou"
            }
        ]
    },
    {
        "id": "bi",
        "en": "Burundi",
        "de": "Burundi",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "kh",
        "en": "Cambodia",
        "de": "Kambodscha",
        "languages": [
            {
                "id": "km",
                "origin": "ភាសាខ្មែរ",
                "name": "Khmer"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1821306,
                "country_id": "kh",
                "origin": "Phnom Penh",
                "ascii": "Phnom Penh",
                "en": "Phnom Penh",
                "de": "Phnom Penh"
            }
        ]
    },
    {
        "id": "cm",
        "en": "Cameroon",
        "de": "Kamerun",
        "languages": [
            {
                "id": "fr",
                "origin": "français, langue française",
                "name": "French"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2220957,
                "country_id": "cm",
                "origin": "Yaoundé",
                "ascii": "Yaounde",
                "en": "Yaounde",
                "de": "Yaoundé"
            },
            {
                "id": 2232593,
                "country_id": "cm",
                "origin": "Douala",
                "ascii": "Douala",
                "en": "Douala",
                "de": "Douala"
            }
        ]
    },
    {
        "id": "ca",
        "en": "Canada",
        "de": "Kanada",
        "languages": [
            {
                "id": "ca",
                "origin": "Català",
                "name": "English (Canada)"
            },
            {
                "id": "qu",
                "origin": "Runa Simi, Kichwa",
                "name": "French (Canada)"
            }
        ],
        "cities": [
            {
                "id": 5946768,
                "country_id": "ca",
                "origin": "Edmonton",
                "ascii": "Edmonton",
                "en": "Edmonton",
                "de": "Edmonton"
            },
            {
                "id": 6077243,
                "country_id": "ca",
                "origin": "Montréal",
                "ascii": "Montreal",
                "en": "Montreal",
                "de": "Montreal"
            },
            {
                "id": 6167865,
                "country_id": "ca",
                "origin": "Toronto",
                "ascii": "Toronto",
                "en": "Toronto",
                "de": "Toronto"
            }
        ]
    },
    {
        "id": "cv",
        "en": "Cabo verde",
        "de": "Kap verde",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "cf",
        "en": "Central african republic",
        "de": "Zentralafrikanische republik",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "td",
        "en": "Chad",
        "de": "Tschad",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2427123,
                "country_id": "td",
                "origin": "N'Djamena",
                "ascii": "N'Djamena",
                "en": "N'Djamena",
                "de": "N’Djamena"
            }
        ]
    },
    {
        "id": "cl",
        "en": "Chile",
        "de": "Chile",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3871336,
                "country_id": "cl",
                "origin": "Santiago",
                "ascii": "Santiago",
                "en": "Santiago",
                "de": "Santiago"
            }
        ]
    },
    {
        "id": "cn",
        "en": "China",
        "de": "China, volksrepublik",
        "languages": [
            {
                "id": "cn",
                "origin": null,
                "name": "Chinese (simplified)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1529102,
                "country_id": "cn",
                "origin": "Ürümqi",
                "ascii": "UEruemqi",
                "en": "Urumqi",
                "de": "Ürümqi"
            },
            {
                "id": 1783621,
                "country_id": "cn",
                "origin": "Zunyi",
                "ascii": "Zunyi",
                "en": "Zunyi",
                "de": "Zunyi"
            },
            {
                "id": 1783763,
                "country_id": "cn",
                "origin": "Zhuzhou",
                "ascii": "Zhuzhou",
                "en": "Zhuzhou",
                "de": "Zhuzhou"
            },
            {
                "id": 1784658,
                "country_id": "cn",
                "origin": "Zhengzhou",
                "ascii": "Zhengzhou",
                "en": "Zhengzhou",
                "de": "Zhengzhou"
            },
            {
                "id": 1784853,
                "country_id": "cn",
                "origin": "Zhaoqing",
                "ascii": "Zhaoqing",
                "en": "Zhaoqing",
                "de": "Zhaoqing"
            },
            {
                "id": 1784990,
                "country_id": "cn",
                "origin": "Zhanjiang",
                "ascii": "Zhanjiang",
                "en": "Zhanjiang",
                "de": "Zhanjiang"
            },
            {
                "id": 1785294,
                "country_id": "cn",
                "origin": "Anyang",
                "ascii": "Anyang",
                "en": "Anyang",
                "de": "Anyang"
            },
            {
                "id": 1785623,
                "country_id": "cn",
                "origin": "Kunshan",
                "ascii": "Kunshan",
                "en": "Kunshan",
                "de": "Kunshan"
            },
            {
                "id": 1785725,
                "country_id": "cn",
                "origin": "Yunfu",
                "ascii": "Yunfu",
                "en": "Yunfu",
                "de": "Yunfu"
            },
            {
                "id": 1785781,
                "country_id": "cn",
                "origin": "Yulin",
                "ascii": "Yulin",
                "en": "Yulin",
                "de": "Yulin"
            },
            {
                "id": 1786217,
                "country_id": "cn",
                "origin": "Yongzhou",
                "ascii": "Yongzhou",
                "en": "Yongzhou",
                "de": "Yongzhou"
            },
            {
                "id": 1786657,
                "country_id": "cn",
                "origin": "Yinchuan",
                "ascii": "Yinchuan",
                "en": "Yinchuan",
                "de": "Yinchuan"
            },
            {
                "id": 1786746,
                "country_id": "cn",
                "origin": "Yichun",
                "ascii": "Yichun",
                "en": "Yichun",
                "de": "Yichun"
            },
            {
                "id": 1786760,
                "country_id": "cn",
                "origin": "Yixing",
                "ascii": "Yixing",
                "en": "Yixing",
                "de": "Yixing"
            },
            {
                "id": 1786764,
                "country_id": "cn",
                "origin": "Yichang",
                "ascii": "Yichang",
                "en": "Yichang",
                "de": "Yichang"
            },
            {
                "id": 1787331,
                "country_id": "cn",
                "origin": "Zhangjiagang",
                "ascii": "Zhangjiagang",
                "en": "Zhangjiagang",
                "de": "Zhangjiagang"
            },
            {
                "id": 1787746,
                "country_id": "cn",
                "origin": "Yancheng",
                "ascii": "Yancheng",
                "en": "Yancheng",
                "de": "Yancheng"
            },
            {
                "id": 1787858,
                "country_id": "cn",
                "origin": "Shangrao",
                "ascii": "Shangrao",
                "en": "Shangrao",
                "de": "Shangrao"
            },
            {
                "id": 1788046,
                "country_id": "cn",
                "origin": "Xuchang",
                "ascii": "Xuchang",
                "en": "Xuchang",
                "de": "Xuchang"
            },
            {
                "id": 1788572,
                "country_id": "cn",
                "origin": "Xinxiang",
                "ascii": "Xinxiang",
                "en": "Xinxiang",
                "de": "Xinxiang"
            },
            {
                "id": 1788852,
                "country_id": "cn",
                "origin": "Xining",
                "ascii": "Xining",
                "en": "Xining",
                "de": "Xining"
            },
            {
                "id": 1790353,
                "country_id": "cn",
                "origin": "Xianyang",
                "ascii": "Xianyang",
                "en": "Xianyang",
                "de": "Xianyang"
            },
            {
                "id": 1790437,
                "country_id": "cn",
                "origin": "Zhuhai",
                "ascii": "Zhuhai",
                "en": "Zhuhai",
                "de": "Zhuhai"
            },
            {
                "id": 1790587,
                "country_id": "cn",
                "origin": "Xiangyang",
                "ascii": "Xiangyang",
                "en": "Xiangyang",
                "de": "Xiangyang"
            },
            {
                "id": 1790630,
                "country_id": "cn",
                "origin": "Xi’an",
                "ascii": "Xi'an",
                "en": "Xi'an",
                "de": "Xi'an"
            },
            {
                "id": 1790645,
                "country_id": "cn",
                "origin": "Xiamen",
                "ascii": "Xiamen",
                "en": "Amoy",
                "de": "Xiamen"
            },
            {
                "id": 1790923,
                "country_id": "cn",
                "origin": "Wuxi",
                "ascii": "Wuxi",
                "en": "Wuxi",
                "de": "Wuxi"
            },
            {
                "id": 1791121,
                "country_id": "cn",
                "origin": "Changde",
                "ascii": "Changde",
                "en": "Changde",
                "de": "Changde"
            },
            {
                "id": 1791236,
                "country_id": "cn",
                "origin": "Wuhu",
                "ascii": "Wuhu",
                "en": "Wuhu",
                "de": "Wuhu"
            },
            {
                "id": 1791247,
                "country_id": "cn",
                "origin": "Wuhan",
                "ascii": "Wuhan",
                "en": "Wuhan",
                "de": "Wuhan"
            },
            {
                "id": 1791388,
                "country_id": "cn",
                "origin": "Wenzhou",
                "ascii": "Wenzhou",
                "en": "Wenzhou",
                "de": "Wenzhou"
            },
            {
                "id": 1791636,
                "country_id": "cn",
                "origin": "Weinan",
                "ascii": "Weinan",
                "en": "Weinan",
                "de": "Weinan"
            },
            {
                "id": 1792892,
                "country_id": "cn",
                "origin": "Tianshui",
                "ascii": "Tianshui",
                "en": "Tianshui",
                "de": "Tianshui"
            },
            {
                "id": 1792947,
                "country_id": "cn",
                "origin": "Tianjin",
                "ascii": "Tianjin",
                "en": "Tianjin",
                "de": "Tianjin"
            },
            {
                "id": 1793346,
                "country_id": "cn",
                "origin": "Tangshan",
                "ascii": "Tangshan",
                "en": "Tangshan",
                "de": "Tangshan"
            },
            {
                "id": 1793505,
                "country_id": "cn",
                "origin": "Taizhou",
                "ascii": "Taizhou",
                "en": "Taizhou",
                "de": "Taizhou"
            },
            {
                "id": 1793511,
                "country_id": "cn",
                "origin": "Taiyuan",
                "ascii": "Taiyuan",
                "en": "Taiyuan",
                "de": "Taiyuan"
            },
            {
                "id": 1793724,
                "country_id": "cn",
                "origin": "Tai’an",
                "ascii": "Tai'an",
                "en": "Tai'an",
                "de": "Tai'an"
            },
            {
                "id": 1793743,
                "country_id": "cn",
                "origin": "Suzhou",
                "ascii": "Suzhou",
                "en": "Suzhou",
                "de": "Suzhou"
            },
            {
                "id": 1793771,
                "country_id": "cn",
                "origin": "Suqian",
                "ascii": "Suqian",
                "en": "Suqian",
                "de": "Suqian"
            },
            {
                "id": 1794903,
                "country_id": "cn",
                "origin": "Shiyan",
                "ascii": "Shiyan",
                "en": "Shiyan",
                "de": "Shiyan"
            },
            {
                "id": 1795270,
                "country_id": "cn",
                "origin": "Shijiazhuang",
                "ascii": "Shijiazhuang",
                "en": "Shijiazhuang",
                "de": "Shijiazhuang"
            },
            {
                "id": 1795565,
                "country_id": "cn",
                "origin": "Shenzhen",
                "ascii": "Shenzhen",
                "en": "Shenzhen",
                "de": "Shenzhen"
            },
            {
                "id": 1795855,
                "country_id": "cn",
                "origin": "Shaoxing",
                "ascii": "Shaoxing",
                "en": "Shaoxing",
                "de": "Shaoxing"
            },
            {
                "id": 1795874,
                "country_id": "cn",
                "origin": "Shaoguan",
                "ascii": "Shaoguan",
                "en": "Shaoguan",
                "de": "Shaoguan"
            },
            {
                "id": 1795940,
                "country_id": "cn",
                "origin": "Shantou",
                "ascii": "Shantou",
                "en": "Shantou",
                "de": "Shantou"
            },
            {
                "id": 1796236,
                "country_id": "cn",
                "origin": "Shanghai",
                "ascii": "Shanghai",
                "en": "Shanghai",
                "de": "Shanghai"
            },
            {
                "id": 1796556,
                "country_id": "cn",
                "origin": "Sanya",
                "ascii": "Sanya",
                "en": "Sanya",
                "de": "Sanya"
            },
            {
                "id": 1797121,
                "country_id": "cn",
                "origin": "Jieyang",
                "ascii": "Jieyang",
                "en": "Jieyang",
                "de": "Jieyang"
            },
            {
                "id": 1797353,
                "country_id": "cn",
                "origin": "Quanzhou",
                "ascii": "Quanzhou",
                "en": "Quanzhou",
                "de": "Quanzhou"
            },
            {
                "id": 1797551,
                "country_id": "cn",
                "origin": "Qinzhou",
                "ascii": "Qinzhou",
                "en": "Qinzhou",
                "de": "Qinzhou"
            },
            {
                "id": 1797658,
                "country_id": "cn",
                "origin": "Jinjiang",
                "ascii": "Jinjiang",
                "en": "Jinjiang",
                "de": "Jinjiang"
            },
            {
                "id": 1797929,
                "country_id": "cn",
                "origin": "Qingdao",
                "ascii": "Qingdao",
                "en": "Qingdao",
                "de": "Qingdao"
            },
            {
                "id": 1797945,
                "country_id": "cn",
                "origin": "Qingyuan",
                "ascii": "Qingyuan",
                "en": "Qingyuan",
                "de": "Qingyuan"
            },
            {
                "id": 1798425,
                "country_id": "cn",
                "origin": "Puyang",
                "ascii": "Puyang",
                "en": "Puyang",
                "de": "Puyang"
            },
            {
                "id": 1798449,
                "country_id": "cn",
                "origin": "Putian",
                "ascii": "Putian",
                "en": "Putian",
                "de": "Putian"
            },
            {
                "id": 1799397,
                "country_id": "cn",
                "origin": "Ningbo",
                "ascii": "Ningbo",
                "en": "Ningbo",
                "de": "Ningbo"
            },
            {
                "id": 1799491,
                "country_id": "cn",
                "origin": "Neijiang",
                "ascii": "Neijiang",
                "en": "Neijiang",
                "de": null
            },
            {
                "id": 1799629,
                "country_id": "cn",
                "origin": "Nanyang",
                "ascii": "Nanyang",
                "en": "Nanyang",
                "de": "Nanyang"
            },
            {
                "id": 1799722,
                "country_id": "cn",
                "origin": "Nantong",
                "ascii": "Nantong",
                "en": "Nantong",
                "de": "Nantong"
            },
            {
                "id": 1799869,
                "country_id": "cn",
                "origin": "Nanning",
                "ascii": "Nanning",
                "en": "Nanning",
                "de": "Nanning"
            },
            {
                "id": 1799962,
                "country_id": "cn",
                "origin": "Nanjing",
                "ascii": "Nanjing",
                "en": "Nanjing",
                "de": "Nanjing"
            },
            {
                "id": 1800146,
                "country_id": "cn",
                "origin": "Nanchong",
                "ascii": "Nanchong",
                "en": "Nanchong",
                "de": "Nanchong"
            },
            {
                "id": 1800163,
                "country_id": "cn",
                "origin": "Nanchang",
                "ascii": "Nanchang",
                "en": "Nanchang",
                "de": "Nanchang"
            },
            {
                "id": 1800627,
                "country_id": "cn",
                "origin": "Mianyang",
                "ascii": "Mianyang",
                "en": "Mianyang",
                "de": "Mianyang"
            },
            {
                "id": 1800818,
                "country_id": "cn",
                "origin": "Meishan",
                "ascii": "Meishan",
                "en": "Meishan",
                "de": "Meishan"
            },
            {
                "id": 1801180,
                "country_id": "cn",
                "origin": "Maoming",
                "ascii": "Maoming",
                "en": "Maoming",
                "de": "Maoming"
            },
            {
                "id": 1801934,
                "country_id": "cn",
                "origin": "Luohe",
                "ascii": "Luohe",
                "en": "Luohe",
                "de": "Luohe"
            },
            {
                "id": 1802206,
                "country_id": "cn",
                "origin": "Lu’an",
                "ascii": "Lu'an",
                "en": "Lu'an",
                "de": "Lu’an"
            },
            {
                "id": 1802276,
                "country_id": "cn",
                "origin": "Longyan",
                "ascii": "Longyan",
                "en": "Longyan",
                "de": "Longyan"
            },
            {
                "id": 1802875,
                "country_id": "cn",
                "origin": "Guankou",
                "ascii": "Guankou",
                "en": "Guankou",
                "de": null
            },
            {
                "id": 1803300,
                "country_id": "cn",
                "origin": "Liuzhou",
                "ascii": "Liuzhou",
                "en": "Liuzhou",
                "de": "Liuzhou"
            },
            {
                "id": 1803318,
                "country_id": "cn",
                "origin": "Linyi",
                "ascii": "Linyi",
                "en": "Linyi",
                "de": "Linyi"
            },
            {
                "id": 1803834,
                "country_id": "cn",
                "origin": "Liaocheng",
                "ascii": "Liaocheng",
                "en": "Liaocheng",
                "de": "Liaocheng"
            },
            {
                "id": 1803936,
                "country_id": "cn",
                "origin": "Wuwei",
                "ascii": "Wuwei",
                "en": "Wuwei",
                "de": "Wuwei"
            },
            {
                "id": 1804430,
                "country_id": "cn",
                "origin": "Lanzhou",
                "ascii": "Lanzhou",
                "en": "Lanzhou",
                "de": "Lanzhou"
            },
            {
                "id": 1804651,
                "country_id": "cn",
                "origin": "Kunming",
                "ascii": "Kunming",
                "en": "Kunming",
                "de": "Kunming"
            },
            {
                "id": 1805179,
                "country_id": "cn",
                "origin": "Jiujiang",
                "ascii": "Jiujiang",
                "en": "Jiujiang",
                "de": "Jiujiang"
            },
            {
                "id": 1805528,
                "country_id": "cn",
                "origin": "Jinhua",
                "ascii": "Jinhua",
                "en": "Jinhua",
                "de": "Jinhua"
            },
            {
                "id": 1805540,
                "country_id": "cn",
                "origin": "Jingzhou",
                "ascii": "Jingzhou",
                "en": "Jingzhou",
                "de": "Jingzhou"
            },
            {
                "id": 1805753,
                "country_id": "cn",
                "origin": "Jinan",
                "ascii": "Jinan",
                "en": "Jinan",
                "de": "Jinan"
            },
            {
                "id": 1805953,
                "country_id": "cn",
                "origin": "Jiaxing",
                "ascii": "Jiaxing",
                "en": "Jiaxing",
                "de": "Jiaxing"
            },
            {
                "id": 1806299,
                "country_id": "cn",
                "origin": "Jiangmen",
                "ascii": "Jiangmen",
                "en": "Jiangmen",
                "de": "Jiangmen"
            },
            {
                "id": 1806408,
                "country_id": "cn",
                "origin": "Yangjiang",
                "ascii": "Yangjiang",
                "en": "Yangjiang",
                "de": "Yangjiang"
            },
            {
                "id": 1806535,
                "country_id": "cn",
                "origin": "Huzhou",
                "ascii": "Huzhou",
                "en": "Huzhou",
                "de": "Huzhou"
            },
            {
                "id": 1806602,
                "country_id": "cn",
                "origin": "Cixi",
                "ascii": "Cixi",
                "en": "Cixi",
                "de": "Cixi"
            },
            {
                "id": 1806776,
                "country_id": "cn",
                "origin": "Huizhou",
                "ascii": "Huizhou",
                "en": "Huizhou",
                "de": "Huizhou"
            },
            {
                "id": 1807700,
                "country_id": "cn",
                "origin": "Huaibei",
                "ascii": "Huaibei",
                "en": "Huaibei",
                "de": "Huaibei"
            },
            {
                "id": 1808198,
                "country_id": "cn",
                "origin": "Heze",
                "ascii": "Heze",
                "en": "Heze",
                "de": "Heze"
            },
            {
                "id": 1808316,
                "country_id": "cn",
                "origin": "Yiyang",
                "ascii": "Yiyang",
                "en": "Yiyang",
                "de": "Yiyang"
            },
            {
                "id": 1808722,
                "country_id": "cn",
                "origin": "Hefei",
                "ascii": "Hefei",
                "en": "Hefei",
                "de": "Hefei"
            },
            {
                "id": 1808857,
                "country_id": "cn",
                "origin": "Hanzhong",
                "ascii": "Hanzhong",
                "en": "Hanzhong",
                "de": "Hanzhong"
            },
            {
                "id": 1808926,
                "country_id": "cn",
                "origin": "Hangzhou",
                "ascii": "Hangzhou",
                "en": "Hangzhou",
                "de": "Hangzhou"
            },
            {
                "id": 1808956,
                "country_id": "cn",
                "origin": "Changzhi",
                "ascii": "Changzhi",
                "en": "Changzhi",
                "de": "Changzhi"
            },
            {
                "id": 1808963,
                "country_id": "cn",
                "origin": "Handan",
                "ascii": "Handan",
                "en": "Handan",
                "de": "Handan"
            },
            {
                "id": 1809078,
                "country_id": "cn",
                "origin": "Haikou",
                "ascii": "Haikou",
                "en": "Haikou",
                "de": "Haikou"
            },
            {
                "id": 1809461,
                "country_id": "cn",
                "origin": "Guiyang",
                "ascii": "Guiyang",
                "en": "Guiyang",
                "de": "Guiyang"
            },
            {
                "id": 1809498,
                "country_id": "cn",
                "origin": "Guilin",
                "ascii": "Guilin",
                "en": "Guilin",
                "de": "Guilin"
            },
            {
                "id": 1809532,
                "country_id": "cn",
                "origin": "Guigang",
                "ascii": "Guigang",
                "en": "Guigang",
                "de": "Guigang"
            },
            {
                "id": 1809858,
                "country_id": "cn",
                "origin": "Guangzhou",
                "ascii": "Guangzhou",
                "en": "Guangzhou",
                "de": "Guangzhou"
            },
            {
                "id": 1810638,
                "country_id": "cn",
                "origin": "Ganzhou",
                "ascii": "Ganzhou",
                "en": "Ganzhou",
                "de": "Ganzhou"
            },
            {
                "id": 1810820,
                "country_id": "cn",
                "origin": "Fuzhou",
                "ascii": "Fuzhou",
                "en": "Fuzhou",
                "de": "Fuzhou"
            },
            {
                "id": 1810821,
                "country_id": "cn",
                "origin": "Fuzhou",
                "ascii": "Fuzhou",
                "en": "Fuzhou",
                "de": "Fuzhou"
            },
            {
                "id": 1810845,
                "country_id": "cn",
                "origin": "Fuyang",
                "ascii": "Fuyang",
                "en": "Fuyang",
                "de": "Fuyang"
            },
            {
                "id": 1811103,
                "country_id": "cn",
                "origin": "Foshan",
                "ascii": "Foshan",
                "en": "Foshan",
                "de": "Foshan"
            },
            {
                "id": 1812545,
                "country_id": "cn",
                "origin": "Dongguan",
                "ascii": "Dongguan",
                "en": "Dongguan",
                "de": "Dongguan"
            },
            {
                "id": 1813325,
                "country_id": "cn",
                "origin": "Dazhou",
                "ascii": "Dazhou",
                "en": "Dazhou",
                "de": null
            },
            {
                "id": 1814870,
                "country_id": "cn",
                "origin": "Yiwu",
                "ascii": "Yiwu",
                "en": "Yiwu",
                "de": "Yiwu"
            },
            {
                "id": 1814906,
                "country_id": "cn",
                "origin": "Chongqing",
                "ascii": "Chongqing",
                "en": "Chongqing",
                "de": "Chongqing"
            },
            {
                "id": 1815251,
                "country_id": "cn",
                "origin": "Jiangyin",
                "ascii": "Jiangyin",
                "en": "Jiangyin",
                "de": "Jiangyin"
            },
            {
                "id": 1815286,
                "country_id": "cn",
                "origin": "Chengdu",
                "ascii": "Chengdu",
                "en": "Chengdu",
                "de": "Chengdu"
            },
            {
                "id": 1815395,
                "country_id": "cn",
                "origin": "Chaozhou",
                "ascii": "Chaozhou",
                "en": "Chaozhou",
                "de": "Chaozhou"
            },
            {
                "id": 1815456,
                "country_id": "cn",
                "origin": "Changzhou",
                "ascii": "Changzhou",
                "en": "Changzhou",
                "de": "Changzhou"
            },
            {
                "id": 1815577,
                "country_id": "cn",
                "origin": "Changsha",
                "ascii": "Changsha",
                "en": "Changsha",
                "de": "Changsha"
            },
            {
                "id": 1816234,
                "country_id": "cn",
                "origin": "Bozhou",
                "ascii": "Bozhou",
                "en": "Bozhou",
                "de": "Bozhou"
            },
            {
                "id": 1816373,
                "country_id": "cn",
                "origin": "Bijie",
                "ascii": "Bijie",
                "en": "Bijie",
                "de": null
            },
            {
                "id": 1816670,
                "country_id": "cn",
                "origin": "Beijing",
                "ascii": "Beijing",
                "en": "Beijing",
                "de": "Beijing"
            },
            {
                "id": 1816971,
                "country_id": "cn",
                "origin": "Baoding",
                "ascii": "Baoding",
                "en": "Baoding",
                "de": "Baoding"
            },
            {
                "id": 1886760,
                "country_id": "cn",
                "origin": "Suzhou",
                "ascii": "Suzhou",
                "en": "Suzhou",
                "de": "Suzhou"
            },
            {
                "id": 2034937,
                "country_id": "cn",
                "origin": "Shenyang",
                "ascii": "Shenyang",
                "en": "Shenyang",
                "de": "Shenyang"
            },
            {
                "id": 2036502,
                "country_id": "cn",
                "origin": "Jilin",
                "ascii": "Jilin",
                "en": "Jilin",
                "de": "Jilin"
            },
            {
                "id": 2036892,
                "country_id": "cn",
                "origin": "Hohhot",
                "ascii": "Hohhot",
                "en": "Hohhot",
                "de": "Hohhot"
            },
            {
                "id": 2037013,
                "country_id": "cn",
                "origin": "Harbin",
                "ascii": "Harbin",
                "en": "Harbin",
                "de": "Harbin"
            },
            {
                "id": 2037355,
                "country_id": "cn",
                "origin": "Fushun",
                "ascii": "Fushun",
                "en": "Fushun",
                "de": "Fushun"
            },
            {
                "id": 2037860,
                "country_id": "cn",
                "origin": "Daqing",
                "ascii": "Daqing",
                "en": "Daqing",
                "de": "Daqing"
            },
            {
                "id": 2038180,
                "country_id": "cn",
                "origin": "Changchun",
                "ascii": "Changchun",
                "en": "Changchun",
                "de": "Chángchūn"
            },
            {
                "id": 6986104,
                "country_id": "cn",
                "origin": "Zhongshan",
                "ascii": "Zhongshan",
                "en": "Zhongshan",
                "de": "Zhongshan"
            },
            {
                "id": 7283386,
                "country_id": "cn",
                "origin": "Changshu",
                "ascii": "Changshu",
                "en": "Changshu",
                "de": "Changshu"
            },
            {
                "id": 7576887,
                "country_id": "cn",
                "origin": "Hezhou",
                "ascii": "Hezhou",
                "en": "Hezhou",
                "de": "Hezhou"
            },
            {
                "id": 7602670,
                "country_id": "cn",
                "origin": "Zhu Cheng City",
                "ascii": "Zhu Cheng City",
                "en": "Zhu Cheng City",
                "de": null
            },
            {
                "id": 8400694,
                "country_id": "cn",
                "origin": "Taizhou",
                "ascii": "Taizhou",
                "en": "Taizhou",
                "de": "Taizhou"
            },
            {
                "id": 10630003,
                "country_id": "cn",
                "origin": "Xuzhou",
                "ascii": "Xuzhou",
                "en": "Xuzhou",
                "de": "Xuzhou"
            },
            {
                "id": 10859300,
                "country_id": "cn",
                "origin": "Lianyungang",
                "ascii": "Lianyungang",
                "en": "Lianyungang",
                "de": "Lianyungang"
            },
            {
                "id": 10942283,
                "country_id": "cn",
                "origin": "Jinzhong",
                "ascii": "Jinzhong",
                "en": "Jinzhong",
                "de": "Jinzhong"
            },
            {
                "id": 10942359,
                "country_id": "cn",
                "origin": "Baoji",
                "ascii": "Baoji",
                "en": "Baoji",
                "de": "Baoji"
            }
        ]
    },
    {
        "id": "co",
        "en": "Colombia",
        "de": "Kolumbien",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3674962,
                "country_id": "co",
                "origin": "Medellín",
                "ascii": "Medellin",
                "en": "Medellin",
                "de": "Medellín"
            },
            {
                "id": 3687925,
                "country_id": "co",
                "origin": "Cali",
                "ascii": "Cali",
                "en": "Santiago de Cali",
                "de": "Cali"
            },
            {
                "id": 3688689,
                "country_id": "co",
                "origin": "Bogotá",
                "ascii": "Bogota",
                "en": "Bogota",
                "de": "Bogotá"
            },
            {
                "id": 3689147,
                "country_id": "co",
                "origin": "Barranquilla",
                "ascii": "Barranquilla",
                "en": "Barranquilla",
                "de": "Barranquilla"
            }
        ]
    },
    {
        "id": "km",
        "en": "Comoros",
        "de": "Komoren",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "cg",
        "en": "Congo",
        "de": "Kongo, republik",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2255414,
                "country_id": "cg",
                "origin": "Pointe-Noire",
                "ascii": "Pointe-Noire",
                "en": "Pointe-Noire",
                "de": "Pointe-Noire"
            },
            {
                "id": 2260535,
                "country_id": "cg",
                "origin": "Brazzaville",
                "ascii": "Brazzaville",
                "en": "Brazzaville",
                "de": "Brazzaville"
            }
        ]
    },
    {
        "id": "cd",
        "en": "Congo, democratic republic of the",
        "de": "Kongo, demokratische republik",
        "languages": [
            {
                "id": "fr",
                "origin": "français, langue française",
                "name": "French"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 209228,
                "country_id": "cd",
                "origin": "Mbuji-Mayi",
                "ascii": "Mbuji-Mayi",
                "en": "Mbuji-Mayi",
                "de": "Mbuji-Mayi"
            },
            {
                "id": 212730,
                "country_id": "cd",
                "origin": "Kisangani",
                "ascii": "Kisangani",
                "en": "Kisangani",
                "de": "Kisangani"
            },
            {
                "id": 214481,
                "country_id": "cd",
                "origin": "Kananga",
                "ascii": "Kananga",
                "en": "Kananga",
                "de": "Kananga"
            },
            {
                "id": 922704,
                "country_id": "cd",
                "origin": "Lubumbashi",
                "ascii": "Lubumbashi",
                "en": "Lubumbashi",
                "de": "Lubumbashi"
            },
            {
                "id": 2314302,
                "country_id": "cd",
                "origin": "Kinshasa",
                "ascii": "Kinshasa",
                "en": "Kinshasa",
                "de": "Kinshasa"
            }
        ]
    },
    {
        "id": "cr",
        "en": "Costa rica",
        "de": "Costa rica",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "ci",
        "en": "Côte d'ivoire",
        "de": "Elfenbeinküste",
        "languages": [
            {
                "id": "fr",
                "origin": "français, langue française",
                "name": "French"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2293538,
                "country_id": "ci",
                "origin": "Abidjan",
                "ascii": "Abidjan",
                "en": "Abidjan",
                "de": "Abidjan"
            }
        ]
    },
    {
        "id": "hr",
        "en": "Croatia",
        "de": "Kroatien",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            },
            {
                "id": "hr",
                "origin": "hrvatski",
                "name": "Croatian"
            }
        ],
        "cities": []
    },
    {
        "id": "cu",
        "en": "Cuba",
        "de": "Kuba",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3553478,
                "country_id": "cu",
                "origin": "Havana",
                "ascii": "Havana",
                "en": "Havana",
                "de": "Havanna"
            }
        ]
    },
    {
        "id": "cy",
        "en": "Cyprus",
        "de": "Zypern",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "cz",
        "en": "Czechia",
        "de": "Tschechien",
        "languages": [
            {
                "id": "cs",
                "origin": "česky, čeština",
                "name": "Czech"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3067696,
                "country_id": "cz",
                "origin": "Prague",
                "ascii": "Prague",
                "en": "Prague",
                "de": "Prag"
            }
        ]
    },
    {
        "id": "dk",
        "en": "Denmark",
        "de": "Dänemark",
        "languages": [
            {
                "id": "da",
                "origin": "dansk",
                "name": "Danish"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2618425,
                "country_id": "dk",
                "origin": "Copenhagen",
                "ascii": "Copenhagen",
                "en": "Copenhagen",
                "de": "Kopenhagen"
            }
        ]
    },
    {
        "id": "dj",
        "en": "Djibouti",
        "de": "Dschibuti",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "dm",
        "en": "Dominica",
        "de": "Dominica",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "do",
        "en": "Dominican republic",
        "de": "Dominikanische republik",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3492908,
                "country_id": "do",
                "origin": "Santo Domingo",
                "ascii": "Santo Domingo",
                "en": "Santo Domingo",
                "de": "Santo Domingo"
            },
            {
                "id": 3492914,
                "country_id": "do",
                "origin": "Santiago de los Caballeros",
                "ascii": "Santiago de los Caballeros",
                "en": "Santiago de los Caballeros",
                "de": "Santiago de los Caballeros"
            }
        ]
    },
    {
        "id": "ec",
        "en": "Ecuador",
        "de": "Ecuador",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3652462,
                "country_id": "ec",
                "origin": "Quito",
                "ascii": "Quito",
                "en": "Quito",
                "de": "Quito"
            },
            {
                "id": 3657509,
                "country_id": "ec",
                "origin": "Guayaquil",
                "ascii": "Guayaquil",
                "en": "Guayaquil",
                "de": "Guayaquil"
            }
        ]
    },
    {
        "id": "eg",
        "en": "Egypt",
        "de": "Ägypten",
        "languages": [
            {
                "id": "ar",
                "origin": "العربية",
                "name": "Arabic"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 349076,
                "country_id": "eg",
                "origin": "Shubrā al Khaymah",
                "ascii": "Shubra al Khaymah",
                "en": "Shubra al Khaymah",
                "de": null
            },
            {
                "id": 360630,
                "country_id": "eg",
                "origin": "Cairo",
                "ascii": "Cairo",
                "en": "Cairo",
                "de": "Kairo"
            },
            {
                "id": 360995,
                "country_id": "eg",
                "origin": "Giza",
                "ascii": "Giza",
                "en": "Giza",
                "de": "Gizeh"
            },
            {
                "id": 361058,
                "country_id": "eg",
                "origin": "Alexandria",
                "ascii": "Alexandria",
                "en": "Alexandria",
                "de": "Alexandria"
            }
        ]
    },
    {
        "id": "sv",
        "en": "El salvador",
        "de": "El salvador",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "gq",
        "en": "Equatorial guinea",
        "de": "Äquatorialguinea",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "er",
        "en": "Eritrea",
        "de": "Eritrea",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "ee",
        "en": "Estonia",
        "de": "Estland",
        "languages": [
            {
                "id": "et",
                "origin": "eesti, eesti keel",
                "name": "Estonian"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "et",
        "en": "Ethiopia",
        "de": "Äthiopien",
        "languages": [
            {
                "id": "am",
                "origin": "አማርኛ",
                "name": "Amharic"
            }
        ],
        "cities": [
            {
                "id": 344979,
                "country_id": "et",
                "origin": "Addis Ababa",
                "ascii": "Addis Ababa",
                "en": "Addis Ababa",
                "de": "Addis Abeba"
            }
        ]
    },
    {
        "id": "fj",
        "en": "Fiji",
        "de": "Fidschi",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "fi",
        "en": "Finland",
        "de": "Finnland",
        "languages": [
            {
                "id": "fi",
                "origin": "suomi, suomen kieli",
                "name": "Finnish"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "fr",
        "en": "France",
        "de": "Frankreich",
        "languages": [
            {
                "id": "fr",
                "origin": "français, langue française",
                "name": "French"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2988507,
                "country_id": "fr",
                "origin": "Paris",
                "ascii": "Paris",
                "en": "Paris",
                "de": "Paris"
            }
        ]
    },
    {
        "id": "ga",
        "en": "Gabon",
        "de": "Gabun",
        "languages": [
            {
                "id": "fr",
                "origin": "français, langue française",
                "name": "French"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "gm",
        "en": "Gambia",
        "de": "Gambia",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "ge",
        "en": "Georgia",
        "de": "Georgien",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 611717,
                "country_id": "ge",
                "origin": "Tbilisi",
                "ascii": "Tbilisi",
                "en": "Tbilisi",
                "de": "Tiflis"
            }
        ]
    },
    {
        "id": "de",
        "en": "Germany",
        "de": "Deutschland",
        "languages": [
            {
                "id": "de",
                "origin": "Deutsch",
                "name": "German"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2867714,
                "country_id": "de",
                "origin": "Munich",
                "ascii": "Munich",
                "en": "Munich",
                "de": "München"
            },
            {
                "id": 2911298,
                "country_id": "de",
                "origin": "Hamburg",
                "ascii": "Hamburg",
                "en": "Hamburg",
                "de": "Hamburg"
            },
            {
                "id": 2950159,
                "country_id": "de",
                "origin": "Berlin",
                "ascii": "Berlin",
                "en": "Berlin",
                "de": "Berlin"
            }
        ]
    },
    {
        "id": "gh",
        "en": "Ghana",
        "de": "Ghana",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2298890,
                "country_id": "gh",
                "origin": "Kumasi",
                "ascii": "Kumasi",
                "en": "Kumasi",
                "de": "Kumasi"
            },
            {
                "id": 2306104,
                "country_id": "gh",
                "origin": "Accra",
                "ascii": "Accra",
                "en": "Accra",
                "de": "Accra"
            }
        ]
    },
    {
        "id": "gr",
        "en": "Greece",
        "de": "Griechenland",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            },
            {
                "id": "el",
                "origin": "Ελληνικά",
                "name": "Greek"
            }
        ],
        "cities": []
    },
    {
        "id": "gd",
        "en": "Grenada",
        "de": "Grenada",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "gt",
        "en": "Guatemala",
        "de": "Guatemala",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "gn",
        "en": "Guinea",
        "de": "Guinea",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2422465,
                "country_id": "gn",
                "origin": "Conakry",
                "ascii": "Conakry",
                "en": "Conakry",
                "de": "Conakry"
            }
        ]
    },
    {
        "id": "gw",
        "en": "Guinea-bissau",
        "de": "Guinea-bissau",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "gy",
        "en": "Guyana",
        "de": "Guyana",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "ht",
        "en": "Haiti",
        "de": "Haiti",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3718426,
                "country_id": "ht",
                "origin": "Port-au-Prince",
                "ascii": "Port-au-Prince",
                "en": "Port-au-Prince",
                "de": "Port-au-Prince"
            }
        ]
    },
    {
        "id": "hn",
        "en": "Honduras",
        "de": "Honduras",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "hu",
        "en": "Hungary",
        "de": "Ungarn",
        "languages": [
            {
                "id": "hu",
                "origin": "Magyar",
                "name": "Hungarian"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3054643,
                "country_id": "hu",
                "origin": "Budapest",
                "ascii": "Budapest",
                "en": "Budapest",
                "de": "Budapest"
            }
        ]
    },
    {
        "id": "is",
        "en": "Iceland",
        "de": "Island",
        "languages": [
            {
                "id": "is",
                "origin": "Íslenska",
                "name": "Icelandic"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "in",
        "en": "India",
        "de": "Indien",
        "languages": [
            {
                "id": "ta",
                "origin": "தமிழ்",
                "name": "Tamil"
            },
            {
                "id": "in",
                "origin": null,
                "name": "English (India)"
            },
            {
                "id": "hi",
                "origin": "हिन्दी, हिंदी",
                "name": "Hindi"
            },
            {
                "id": "bn",
                "origin": "বাংলা",
                "name": "Bengali"
            },
            {
                "id": "mr",
                "origin": "मराठी",
                "name": "Marathi"
            },
            {
                "id": "pa",
                "origin": "ਪੰਜਾਬੀ, پنجابی‎",
                "name": "Punjabi"
            },
            {
                "id": "te",
                "origin": "తెలుగు",
                "name": "Telugu"
            },
            {
                "id": "ml",
                "origin": "മലയാളം",
                "name": "Mayalam"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            },
            {
                "id": "kn",
                "origin": "ಕನ್ನಡ",
                "name": "Kannada"
            }
        ],
        "cities": [
            {
                "id": 1253102,
                "country_id": "in",
                "origin": "Visakhapatnam",
                "ascii": "Visakhapatnam",
                "en": "Visakhapatnam",
                "de": "Visakhapatnam"
            },
            {
                "id": 1254361,
                "country_id": "in",
                "origin": "Tirunelveli",
                "ascii": "Tirunelveli",
                "en": "Tirunelveli",
                "de": "Tirunelveli"
            },
            {
                "id": 1258526,
                "country_id": "in",
                "origin": "Ranchi",
                "ascii": "Ranchi",
                "en": "Ranchi",
                "de": "Ranchi"
            },
            {
                "id": 1260086,
                "country_id": "in",
                "origin": "Patna",
                "ascii": "Patna",
                "en": "Patna",
                "de": "Patna"
            },
            {
                "id": 1261162,
                "country_id": "in",
                "origin": "Nowrangapur",
                "ascii": "Nowrangapur",
                "en": "Nowrangapur",
                "de": null
            },
            {
                "id": 1261731,
                "country_id": "in",
                "origin": "Nashik",
                "ascii": "Nashik",
                "en": "Nashik",
                "de": null
            },
            {
                "id": 1262180,
                "country_id": "in",
                "origin": "Nagpur",
                "ascii": "Nagpur",
                "en": "Nagpur",
                "de": "Nagpur"
            },
            {
                "id": 1264521,
                "country_id": "in",
                "origin": "Madurai",
                "ascii": "Madurai",
                "en": "Madurai",
                "de": "Madurai"
            },
            {
                "id": 1264527,
                "country_id": "in",
                "origin": "Chennai",
                "ascii": "Chennai",
                "en": "Chennai",
                "de": "Chennai"
            },
            {
                "id": 1264733,
                "country_id": "in",
                "origin": "Lucknow",
                "ascii": "Lucknow",
                "en": "Lucknow",
                "de": "Lucknow"
            },
            {
                "id": 1269515,
                "country_id": "in",
                "origin": "Jaipur",
                "ascii": "Jaipur",
                "en": "Jaipur",
                "de": "Jaipur"
            },
            {
                "id": 1269843,
                "country_id": "in",
                "origin": "Hyderābād",
                "ascii": "Hyderabad",
                "en": "Hyderabad",
                "de": "Hyderabad"
            },
            {
                "id": 1271308,
                "country_id": "in",
                "origin": "Ghāziābād",
                "ascii": "Ghaziabad",
                "en": "Ghaziabad",
                "de": "Ghaziabad"
            },
            {
                "id": 1272979,
                "country_id": "in",
                "origin": "Dhanbad",
                "ascii": "Dhanbad",
                "en": "Dhanbad",
                "de": "Dhanbad"
            },
            {
                "id": 1273294,
                "country_id": "in",
                "origin": "Delhi",
                "ascii": "Delhi",
                "en": "Delhi",
                "de": "Delhi"
            },
            {
                "id": 1275004,
                "country_id": "in",
                "origin": "Kolkata",
                "ascii": "Kolkata",
                "en": "Kolkata",
                "de": "Kalkutta"
            },
            {
                "id": 1275339,
                "country_id": "in",
                "origin": "Mumbai",
                "ascii": "Mumbai",
                "en": "Mumbai",
                "de": "Mumbai"
            },
            {
                "id": 1275841,
                "country_id": "in",
                "origin": "Bhopāl",
                "ascii": "Bhopal",
                "en": "Bhopal",
                "de": "Bhopal"
            },
            {
                "id": 1277333,
                "country_id": "in",
                "origin": "Bengaluru",
                "ascii": "Bengaluru",
                "en": "Bengaluru",
                "de": "Bengaluru"
            },
            {
                "id": 1278149,
                "country_id": "in",
                "origin": "Sambhaji Nagar",
                "ascii": "Sambhaji Nagar",
                "en": "Aurangabad",
                "de": "Aurangabad"
            },
            {
                "id": 1279259,
                "country_id": "in",
                "origin": "Agra",
                "ascii": "Agra",
                "en": "Agra",
                "de": "Agra"
            },
            {
                "id": 12165956,
                "country_id": "in",
                "origin": "Kallakurichi",
                "ascii": "Kallakurichi",
                "en": "Kallakurichi",
                "de": null
            }
        ]
    },
    {
        "id": "id",
        "en": "Indonesia",
        "de": "Indonesien",
        "languages": [
            {
                "id": "id",
                "origin": "Bahasa Indonesia",
                "name": "Indonesian"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1214520,
                "country_id": "id",
                "origin": "Medan",
                "ascii": "Medan",
                "en": "Medan",
                "de": "Medan"
            },
            {
                "id": 1622786,
                "country_id": "id",
                "origin": "Makassar",
                "ascii": "Makassar",
                "en": "Makassar",
                "de": "Makassar"
            },
            {
                "id": 1624917,
                "country_id": "id",
                "origin": "Bandar Lampung",
                "ascii": "Bandar Lampung",
                "en": "Bandar Lampung",
                "de": "Bandar Lampung"
            },
            {
                "id": 1625822,
                "country_id": "id",
                "origin": "Surabaya",
                "ascii": "Surabaya",
                "en": "Surabaya",
                "de": "Surabaya"
            },
            {
                "id": 1627896,
                "country_id": "id",
                "origin": "Semarang",
                "ascii": "Semarang",
                "en": "Semarang",
                "de": "Semarang"
            },
            {
                "id": 1631761,
                "country_id": "id",
                "origin": "Pekanbaru",
                "ascii": "Pekanbaru",
                "en": "Pekanbaru",
                "de": "Pekanbaru"
            },
            {
                "id": 1633070,
                "country_id": "id",
                "origin": "Palembang",
                "ascii": "Palembang",
                "en": "Palembang",
                "de": "Palembang"
            },
            {
                "id": 1642548,
                "country_id": "id",
                "origin": "Jepara",
                "ascii": "Jepara",
                "en": "Jepara",
                "de": null
            },
            {
                "id": 1642911,
                "country_id": "id",
                "origin": "Jakarta",
                "ascii": "Jakarta",
                "en": "Jakarta",
                "de": "Jakarta"
            },
            {
                "id": 1650357,
                "country_id": "id",
                "origin": "Bandung",
                "ascii": "Bandung",
                "en": "Bandung",
                "de": "Bandung"
            }
        ]
    },
    {
        "id": "ir",
        "en": "Iran (islamic republic of)",
        "de": "Iran",
        "languages": [
            {
                "id": "fa",
                "origin": "فارسی",
                "name": "Persian"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 112931,
                "country_id": "ir",
                "origin": "Tehran",
                "ascii": "Tehran",
                "en": "Tehran",
                "de": "Teheran"
            },
            {
                "id": 113646,
                "country_id": "ir",
                "origin": "Tabriz",
                "ascii": "Tabriz",
                "en": "Tabriz",
                "de": "Täbris"
            },
            {
                "id": 115019,
                "country_id": "ir",
                "origin": "Shiraz",
                "ascii": "Shiraz",
                "en": "Shiraz",
                "de": "Schiras"
            },
            {
                "id": 124665,
                "country_id": "ir",
                "origin": "Mashhad",
                "ascii": "Mashhad",
                "en": "Mashhad",
                "de": "Mashhad"
            },
            {
                "id": 128747,
                "country_id": "ir",
                "origin": "Karaj",
                "ascii": "Karaj",
                "en": "Karaj",
                "de": "Karadsch"
            },
            {
                "id": 418863,
                "country_id": "ir",
                "origin": "Isfahan",
                "ascii": "Isfahan",
                "en": "Isfahan",
                "de": "Isfahan"
            }
        ]
    },
    {
        "id": "iq",
        "en": "Iraq",
        "de": "Irak",
        "languages": [
            {
                "id": "ar",
                "origin": "العربية",
                "name": "Arabic"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 94787,
                "country_id": "iq",
                "origin": "Kirkuk",
                "ascii": "Kirkuk",
                "en": "Kirkuk",
                "de": "Kirkuk"
            },
            {
                "id": 94824,
                "country_id": "iq",
                "origin": "Karbala",
                "ascii": "Karbala",
                "en": "Karbala",
                "de": "Karbala"
            },
            {
                "id": 95446,
                "country_id": "iq",
                "origin": "Erbil",
                "ascii": "Erbil",
                "en": "Erbil",
                "de": "Arbil"
            },
            {
                "id": 98182,
                "country_id": "iq",
                "origin": "Baghdad",
                "ascii": "Baghdad",
                "en": "Baghdad",
                "de": "Bagdad"
            },
            {
                "id": 99072,
                "country_id": "iq",
                "origin": "Mosul",
                "ascii": "Mosul",
                "en": "Mosul",
                "de": "Mossul"
            },
            {
                "id": 99532,
                "country_id": "iq",
                "origin": "Basrah",
                "ascii": "Basrah",
                "en": "Basra",
                "de": "Basra"
            }
        ]
    },
    {
        "id": "ie",
        "en": "Ireland",
        "de": "Irland",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2964574,
                "country_id": "ie",
                "origin": "Dublin",
                "ascii": "Dublin",
                "en": "Dublin",
                "de": "Dublin"
            }
        ]
    },
    {
        "id": "il",
        "en": "Israel",
        "de": "Israel",
        "languages": [
            {
                "id": "he",
                "origin": "עברית",
                "name": "Hebrew"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "it",
        "en": "Italy",
        "de": "Italien",
        "languages": [
            {
                "id": "it",
                "origin": "Italiano",
                "name": "Italian"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3169070,
                "country_id": "it",
                "origin": "Rome",
                "ascii": "Rome",
                "en": "Rome",
                "de": "Rom"
            },
            {
                "id": 3173435,
                "country_id": "it",
                "origin": "Milan",
                "ascii": "Milan",
                "en": "Milan",
                "de": "Mailand"
            }
        ]
    },
    {
        "id": "jm",
        "en": "Jamaica",
        "de": "Jamaika",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "jp",
        "en": "Japan",
        "de": "Japan",
        "languages": [
            {
                "id": "ja",
                "origin": "日本語 (にほんご／にっぽんご)",
                "name": "Japanese"
            },
            {
                "id": "us",
                "origin": null,
                "name": "English (US)"
            }
        ],
        "cities": [
            {
                "id": 1848354,
                "country_id": "jp",
                "origin": "Yokohama",
                "ascii": "Yokohama",
                "en": "Yokohama",
                "de": "Yokohama"
            },
            {
                "id": 1850147,
                "country_id": "jp",
                "origin": "Tokyo",
                "ascii": "Tokyo",
                "en": "Tokyo",
                "de": "Tokio"
            },
            {
                "id": 1853909,
                "country_id": "jp",
                "origin": "Osaka",
                "ascii": "Osaka",
                "en": "Osaka",
                "de": "Ōsaka"
            },
            {
                "id": 1856057,
                "country_id": "jp",
                "origin": "Nagoya",
                "ascii": "Nagoya",
                "en": "Nagoya",
                "de": "Nagoya"
            },
            {
                "id": 1857910,
                "country_id": "jp",
                "origin": "Kyoto",
                "ascii": "Kyoto",
                "en": "Kyoto",
                "de": "Kyōto"
            },
            {
                "id": 1859171,
                "country_id": "jp",
                "origin": "Kobe",
                "ascii": "Kobe",
                "en": "Kobe",
                "de": "Kōbe"
            },
            {
                "id": 1859642,
                "country_id": "jp",
                "origin": "Kawasaki",
                "ascii": "Kawasaki",
                "en": "Kawasaki",
                "de": "Kawasaki"
            },
            {
                "id": 1862415,
                "country_id": "jp",
                "origin": "Hiroshima",
                "ascii": "Hiroshima",
                "en": "Hiroshima",
                "de": "Hiroshima"
            },
            {
                "id": 1863967,
                "country_id": "jp",
                "origin": "Fukuoka",
                "ascii": "Fukuoka",
                "en": "Fukuoka",
                "de": "Fukuoka"
            },
            {
                "id": 2111149,
                "country_id": "jp",
                "origin": "Sendai",
                "ascii": "Sendai",
                "en": "Sendai",
                "de": "Sendai"
            },
            {
                "id": 2128295,
                "country_id": "jp",
                "origin": "Sapporo",
                "ascii": "Sapporo",
                "en": "Sapporo",
                "de": "Sapporo"
            },
            {
                "id": 6940394,
                "country_id": "jp",
                "origin": "Saitama",
                "ascii": "Saitama",
                "en": "Saitama",
                "de": null
            }
        ]
    },
    {
        "id": "jo",
        "en": "Jordan",
        "de": "Jordanien",
        "languages": [
            {
                "id": "ar",
                "origin": "العربية",
                "name": "Arabic"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 250441,
                "country_id": "jo",
                "origin": "Amman",
                "ascii": "Amman",
                "en": "Amman",
                "de": "Amman"
            }
        ]
    },
    {
        "id": "kz",
        "en": "Kazakhstan",
        "de": "Kasachstan",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1518980,
                "country_id": "kz",
                "origin": "Shymkent",
                "ascii": "Shymkent",
                "en": "Shymkent",
                "de": "Schymkent"
            },
            {
                "id": 1526384,
                "country_id": "kz",
                "origin": "Almaty",
                "ascii": "Almaty",
                "en": "Almaty",
                "de": "Almaty"
            }
        ]
    },
    {
        "id": "ke",
        "en": "Kenya",
        "de": "Kenia",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 184745,
                "country_id": "ke",
                "origin": "Nairobi",
                "ascii": "Nairobi",
                "en": "Nairobi",
                "de": "Nairobi"
            },
            {
                "id": 186301,
                "country_id": "ke",
                "origin": "Mombasa",
                "ascii": "Mombasa",
                "en": "Mombasa",
                "de": "Mombasa"
            },
            {
                "id": 195272,
                "country_id": "ke",
                "origin": "Kakamega",
                "ascii": "Kakamega",
                "en": "Kakamega",
                "de": "Kakamega"
            }
        ]
    },
    {
        "id": "ki",
        "en": "Kiribati",
        "de": "Kiribati",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "kp",
        "en": "Korea (democratic people's republic of)",
        "de": "Korea, nord (nordkorea)",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1871859,
                "country_id": "kp",
                "origin": "Pyongyang",
                "ascii": "Pyongyang",
                "en": "Pyongyang",
                "de": "Pjöngjang"
            }
        ]
    },
    {
        "id": "kr",
        "en": "Korea, republic of",
        "de": "Korea, süd (südkorea)",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            },
            {
                "id": "ko",
                "origin": "한국어 (韓國語), 조선말 (朝鮮語)",
                "name": "Korean"
            }
        ],
        "cities": [
            {
                "id": 1835235,
                "country_id": "kr",
                "origin": "Daejeon",
                "ascii": "Daejeon",
                "en": "Daejeon",
                "de": "Daejeon"
            },
            {
                "id": 1835329,
                "country_id": "kr",
                "origin": "Daegu",
                "ascii": "Daegu",
                "en": "Daegu",
                "de": "Daegu"
            },
            {
                "id": 1835553,
                "country_id": "kr",
                "origin": "Suwon",
                "ascii": "Suwon",
                "en": "Suwon-si",
                "de": "Suwon"
            },
            {
                "id": 1835848,
                "country_id": "kr",
                "origin": "Seoul",
                "ascii": "Seoul",
                "en": "Seoul",
                "de": "Seoul"
            },
            {
                "id": 1838524,
                "country_id": "kr",
                "origin": "Busan",
                "ascii": "Busan",
                "en": "Busan",
                "de": "Busan"
            },
            {
                "id": 1841811,
                "country_id": "kr",
                "origin": "Gwangju",
                "ascii": "Gwangju",
                "en": "Gwangju",
                "de": "Gwangju"
            },
            {
                "id": 1842485,
                "country_id": "kr",
                "origin": "Goyang-si",
                "ascii": "Goyang-si",
                "en": "Goyang-si",
                "de": null
            },
            {
                "id": 1843564,
                "country_id": "kr",
                "origin": "Incheon",
                "ascii": "Incheon",
                "en": "Incheon",
                "de": "Incheon"
            },
            {
                "id": 1846326,
                "country_id": "kr",
                "origin": "Changwon",
                "ascii": "Changwon",
                "en": "Changwon",
                "de": "Changwon"
            }
        ]
    },
    {
        "id": "kw",
        "en": "Kuwait",
        "de": "Kuwait",
        "languages": [
            {
                "id": "ar",
                "origin": "العربية",
                "name": "Arabic"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "kg",
        "en": "Kyrgyzstan",
        "de": "Kirgisistan",
        "languages": [
            {
                "id": "ky",
                "origin": "кыргыз тили",
                "name": "Kirghiz, Kyrgyz"
            }
        ],
        "cities": []
    },
    {
        "id": "la",
        "en": "Lao people's democratic republic",
        "de": "Laos",
        "languages": [
            {
                "id": "lo",
                "origin": "ພາສາລາວ",
                "name": "Lao"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "lv",
        "en": "Latvia",
        "de": "Lettland",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            },
            {
                "id": "lv",
                "origin": "latviešu valoda",
                "name": "Latvian"
            }
        ],
        "cities": []
    },
    {
        "id": "lb",
        "en": "Lebanon",
        "de": "Libanon",
        "languages": [
            {
                "id": "ar",
                "origin": "العربية",
                "name": "Arabic"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 276781,
                "country_id": "lb",
                "origin": "Beirut",
                "ascii": "Beirut",
                "en": "Beirut",
                "de": "Beirut"
            }
        ]
    },
    {
        "id": "ls",
        "en": "Lesotho",
        "de": "Lesotho",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "lr",
        "en": "Liberia",
        "de": "Liberia",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2274895,
                "country_id": "lr",
                "origin": "Monrovia",
                "ascii": "Monrovia",
                "en": "Monrovia",
                "de": "Monrovia"
            }
        ]
    },
    {
        "id": "ly",
        "en": "Libya",
        "de": "Libyen",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2210247,
                "country_id": "ly",
                "origin": "Tripoli",
                "ascii": "Tripoli",
                "en": "Tripoli",
                "de": "Tripolis"
            }
        ]
    },
    {
        "id": "li",
        "en": "Liechtenstein",
        "de": "Liechtenstein",
        "languages": [
            {
                "id": "de",
                "origin": "Deutsch",
                "name": "German"
            }
        ],
        "cities": []
    },
    {
        "id": "lt",
        "en": "Lithuania",
        "de": "Litauen",
        "languages": [
            {
                "id": "lt",
                "origin": "lietuvių kalba",
                "name": "Lithuanian"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "lu",
        "en": "Luxembourg",
        "de": "Luxemburg",
        "languages": [
            {
                "id": "de",
                "origin": "Deutsch",
                "name": "German"
            },
            {
                "id": "fr",
                "origin": "français, langue française",
                "name": "French"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "mk",
        "en": "North macedonia",
        "de": "Nordmazedonien",
        "languages": [
            {
                "id": "mk",
                "origin": "македонски јазик",
                "name": "Macedonian"
            }
        ],
        "cities": []
    },
    {
        "id": "mg",
        "en": "Madagascar",
        "de": "Madagaskar",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1070940,
                "country_id": "mg",
                "origin": "Antananarivo",
                "ascii": "Antananarivo",
                "en": "Antananarivo",
                "de": "Antananarivo"
            }
        ]
    },
    {
        "id": "mw",
        "en": "Malawi",
        "de": "Malawi",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "my",
        "en": "Malaysia",
        "de": "Malaysia",
        "languages": [
            {
                "id": "cn",
                "origin": null,
                "name": "Chinese (simplified)"
            },
            {
                "id": "ms",
                "origin": "bahasa Melayu, بهاس ملايو‎",
                "name": "Malay"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1735161,
                "country_id": "my",
                "origin": "Kuala Lumpur",
                "ascii": "Kuala Lumpur",
                "en": "Kuala Lumpur",
                "de": "Kuala Lumpur"
            }
        ]
    },
    {
        "id": "mv",
        "en": "Maldives",
        "de": "Malediven",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "ml",
        "en": "Mali",
        "de": "Mali",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2460596,
                "country_id": "ml",
                "origin": "Bamako",
                "ascii": "Bamako",
                "en": "Bamako",
                "de": "Bamako"
            }
        ]
    },
    {
        "id": "mt",
        "en": "Malta",
        "de": "Malta",
        "languages": [
            {
                "id": "mt",
                "origin": "Malti",
                "name": "Maltese"
            }
        ],
        "cities": []
    },
    {
        "id": "mh",
        "en": "Marshall islands",
        "de": "Marshallinseln",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "mr",
        "en": "Mauritania",
        "de": "Mauretanien",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "mu",
        "en": "Mauritius",
        "de": "Mauritius",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "mx",
        "en": "Mexico",
        "de": "Mexiko",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3521081,
                "country_id": "mx",
                "origin": "Puebla",
                "ascii": "Puebla",
                "en": "Puebla",
                "de": "Puebla"
            },
            {
                "id": 3523349,
                "country_id": "mx",
                "origin": "Mérida",
                "ascii": "Merida",
                "en": "Merida",
                "de": "Mérida"
            },
            {
                "id": 3529612,
                "country_id": "mx",
                "origin": "Ecatepec de Morelos",
                "ascii": "Ecatepec de Morelos",
                "en": "Ecatepec de Morelos",
                "de": "Ecatepec de Morelos"
            },
            {
                "id": 3530597,
                "country_id": "mx",
                "origin": "Mexico City",
                "ascii": "Mexico City",
                "en": "Mexico City",
                "de": "Mexiko-Stadt"
            },
            {
                "id": 3979770,
                "country_id": "mx",
                "origin": "Zapopan",
                "ascii": "Zapopan",
                "en": "Zapopan",
                "de": "Zapopan"
            },
            {
                "id": 3981609,
                "country_id": "mx",
                "origin": "Tijuana",
                "ascii": "Tijuana",
                "en": "Tijuana",
                "de": "Tijuana"
            },
            {
                "id": 3991164,
                "country_id": "mx",
                "origin": "Santiago de Querétaro",
                "ascii": "Santiago de Queretaro",
                "en": "Santiago de Queretaro",
                "de": null
            },
            {
                "id": 3995465,
                "country_id": "mx",
                "origin": "Monterrey",
                "ascii": "Monterrey",
                "en": "Monterrey",
                "de": "Monterrey"
            },
            {
                "id": 3996069,
                "country_id": "mx",
                "origin": "Mexicali",
                "ascii": "Mexicali",
                "en": "Mexicali",
                "de": "Mexicali"
            },
            {
                "id": 3998655,
                "country_id": "mx",
                "origin": "León de los Aldama",
                "ascii": "Leon de los Aldama",
                "en": "Leon",
                "de": "León"
            },
            {
                "id": 4005539,
                "country_id": "mx",
                "origin": "Guadalajara",
                "ascii": "Guadalajara",
                "en": "Guadalajara",
                "de": "Guadalajara"
            },
            {
                "id": 4013708,
                "country_id": "mx",
                "origin": "Ciudad Juárez",
                "ascii": "Ciudad Juarez",
                "en": "Ciudad Juarez",
                "de": "Ciudad Juárez"
            }
        ]
    },
    {
        "id": "ma",
        "en": "Morocco",
        "de": "Marokko",
        "languages": [
            {
                "id": "fr",
                "origin": "français, langue française",
                "name": "French"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2538475,
                "country_id": "ma",
                "origin": "Rabat",
                "ascii": "Rabat",
                "en": "Rabat",
                "de": "Rabat"
            },
            {
                "id": 2553604,
                "country_id": "ma",
                "origin": "Casablanca",
                "ascii": "Casablanca",
                "en": "Casablanca",
                "de": "Casablanca"
            }
        ]
    },
    {
        "id": "md",
        "en": "Moldova, republic of",
        "de": "Moldau",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "mc",
        "en": "Monaco",
        "de": "Monaco",
        "languages": [
            {
                "id": "fr",
                "origin": "français, langue française",
                "name": "French"
            }
        ],
        "cities": []
    },
    {
        "id": "mn",
        "en": "Mongolia",
        "de": "Mongolei",
        "languages": [
            {
                "id": "mn",
                "origin": "монгол",
                "name": "Mongolian"
            }
        ],
        "cities": []
    },
    {
        "id": "me",
        "en": "Montenegro",
        "de": "Montenegro",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            },
            {
                "id": "hr",
                "origin": "hrvatski",
                "name": "Croatian"
            }
        ],
        "cities": []
    },
    {
        "id": "mz",
        "en": "Mozambique",
        "de": "Mosambik",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1039854,
                "country_id": "mz",
                "origin": "Matola",
                "ascii": "Matola",
                "en": "Matola",
                "de": "Matola"
            },
            {
                "id": 1040652,
                "country_id": "mz",
                "origin": "Maputo",
                "ascii": "Maputo",
                "en": "Maputo",
                "de": "Maputo"
            }
        ]
    },
    {
        "id": "mm",
        "en": "Myanmar",
        "de": "Myanmar",
        "languages": [
            {
                "id": "my",
                "origin": "ဗမာစာ",
                "name": "Burmese"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1298824,
                "country_id": "mm",
                "origin": "Yangon",
                "ascii": "Yangon",
                "en": "Yangon",
                "de": "Rangun"
            },
            {
                "id": 1311874,
                "country_id": "mm",
                "origin": "Mandalay",
                "ascii": "Mandalay",
                "en": "Mandalay",
                "de": "Mandalay"
            }
        ]
    },
    {
        "id": "na",
        "en": "Namibia",
        "de": "Namibia",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "nr",
        "en": "Nauru",
        "de": "Nauru",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "np",
        "en": "Nepal",
        "de": "Nepal",
        "languages": [
            {
                "id": "ne",
                "origin": "नेपाली",
                "name": "Nepali"
            }
        ],
        "cities": [
            {
                "id": 1283240,
                "country_id": "np",
                "origin": "Kathmandu",
                "ascii": "Kathmandu",
                "en": "Kathmandu",
                "de": "Kathmandu"
            }
        ]
    },
    {
        "id": "nl",
        "en": "Netherlands",
        "de": "Niederlande",
        "languages": [
            {
                "id": "nl",
                "origin": "Nederlands, Vlaams",
                "name": "Dutch"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "nz",
        "en": "New zealand",
        "de": "Neuseeland",
        "languages": [
            {
                "id": "au",
                "origin": null,
                "name": "English (Australia)"
            }
        ],
        "cities": []
    },
    {
        "id": "ni",
        "en": "Nicaragua",
        "de": "Nicaragua",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "ne",
        "en": "Niger",
        "de": "Niger",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "ng",
        "en": "Nigeria",
        "de": "Nigeria",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2324774,
                "country_id": "ng",
                "origin": "Port Harcourt",
                "ascii": "Port Harcourt",
                "en": "Port Harcourt",
                "de": "Port Harcourt"
            },
            {
                "id": 2326016,
                "country_id": "ng",
                "origin": "Onitsha",
                "ascii": "Onitsha",
                "en": "Onitsha",
                "de": "Onitsha"
            },
            {
                "id": 2332459,
                "country_id": "ng",
                "origin": "Lagos",
                "ascii": "Lagos",
                "en": "Lagos",
                "de": "Lagos"
            },
            {
                "id": 2335204,
                "country_id": "ng",
                "origin": "Kano",
                "ascii": "Kano",
                "en": "Kano",
                "de": "Kano"
            },
            {
                "id": 2335727,
                "country_id": "ng",
                "origin": "Kaduna",
                "ascii": "Kaduna",
                "en": "Kaduna",
                "de": "Kaduna"
            },
            {
                "id": 2339354,
                "country_id": "ng",
                "origin": "Ibadan",
                "ascii": "Ibadan",
                "en": "Ibadan",
                "de": "Ibadan"
            },
            {
                "id": 2347283,
                "country_id": "ng",
                "origin": "Benin City",
                "ascii": "Benin City",
                "en": "Benin City",
                "de": "Benin-Stadt"
            },
            {
                "id": 2352778,
                "country_id": "ng",
                "origin": "Abuja",
                "ascii": "Abuja",
                "en": "Abuja",
                "de": "Abuja"
            }
        ]
    },
    {
        "id": "no",
        "en": "Norway",
        "de": "Norwegen",
        "languages": [
            {
                "id": "no",
                "origin": "Norsk",
                "name": "Norwegian"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "om",
        "en": "Oman",
        "de": "Oman",
        "languages": [
            {
                "id": "ar",
                "origin": "العربية",
                "name": "Arabic"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "pk",
        "en": "Pakistan",
        "de": "Pakistan",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1166993,
                "country_id": "pk",
                "origin": "Rawalpindi",
                "ascii": "Rawalpindi",
                "en": "Rawalpindi",
                "de": "Rawalpindi"
            },
            {
                "id": 1168197,
                "country_id": "pk",
                "origin": "Peshawar",
                "ascii": "Peshawar",
                "en": "Peshawar",
                "de": "Peschawar"
            },
            {
                "id": 1169825,
                "country_id": "pk",
                "origin": "Multan",
                "ascii": "Multan",
                "en": "Multan",
                "de": "Multan"
            },
            {
                "id": 1172451,
                "country_id": "pk",
                "origin": "Lahore",
                "ascii": "Lahore",
                "en": "Lahore",
                "de": "Lahore"
            },
            {
                "id": 1174872,
                "country_id": "pk",
                "origin": "Karachi",
                "ascii": "Karachi",
                "en": "Karachi",
                "de": "Karatschi"
            },
            {
                "id": 1176734,
                "country_id": "pk",
                "origin": "Hyderabad",
                "ascii": "Hyderabad",
                "en": "Hyderabad",
                "de": "Hyderabad"
            },
            {
                "id": 1177662,
                "country_id": "pk",
                "origin": "Gujranwala",
                "ascii": "Gujranwala",
                "en": "Gujranwala",
                "de": "Gujranwala"
            },
            {
                "id": 1179400,
                "country_id": "pk",
                "origin": "Faisalabad",
                "ascii": "Faisalabad",
                "en": "Faisalabad",
                "de": "Faisalabad"
            }
        ]
    },
    {
        "id": "pw",
        "en": "Palau",
        "de": "Palau",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "pa",
        "en": "Panama",
        "de": "Panama",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "pg",
        "en": "Papua new guinea",
        "de": "Papua-neuguinea",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "py",
        "en": "Paraguay",
        "de": "Paraguay",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3439389,
                "country_id": "py",
                "origin": "Asunción",
                "ascii": "Asuncion",
                "en": "Asuncion",
                "de": "Asunción"
            }
        ]
    },
    {
        "id": "pe",
        "en": "Peru",
        "de": "Peru",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3936456,
                "country_id": "pe",
                "origin": "Lima",
                "ascii": "Lima",
                "en": "Lima",
                "de": "Lima"
            },
            {
                "id": 3946083,
                "country_id": "pe",
                "origin": "Callao",
                "ascii": "Callao",
                "en": "Callao",
                "de": "Callao"
            },
            {
                "id": 3947322,
                "country_id": "pe",
                "origin": "Arequipa",
                "ascii": "Arequipa",
                "en": "Arequipa",
                "de": "Arequipa"
            }
        ]
    },
    {
        "id": "ph",
        "en": "Philippines",
        "de": "Philippinen",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1692192,
                "country_id": "ph",
                "origin": "Quezon City",
                "ascii": "Quezon City",
                "en": "Quezon City",
                "de": null
            },
            {
                "id": 1701668,
                "country_id": "ph",
                "origin": "Manila",
                "ascii": "Manila",
                "en": "Manila",
                "de": "Manila"
            },
            {
                "id": 1715348,
                "country_id": "ph",
                "origin": "Davao",
                "ascii": "Davao",
                "en": "Davao",
                "de": "Davao"
            },
            {
                "id": 1720151,
                "country_id": "ph",
                "origin": "Caloocan City",
                "ascii": "Caloocan City",
                "en": "Caloocan City",
                "de": null
            }
        ]
    },
    {
        "id": "pl",
        "en": "Poland",
        "de": "Polen",
        "languages": [
            {
                "id": "pl",
                "origin": "polski",
                "name": "Polish"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 756135,
                "country_id": "pl",
                "origin": "Warsaw",
                "ascii": "Warsaw",
                "en": "Warsaw",
                "de": "Warschau"
            }
        ]
    },
    {
        "id": "pt",
        "en": "Portugal",
        "de": "Portugal",
        "languages": [
            {
                "id": "pt",
                "origin": "Português",
                "name": "Portuguese"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "qa",
        "en": "Qatar",
        "de": "Katar",
        "languages": [
            {
                "id": "ar",
                "origin": "العربية",
                "name": "Arabic"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "ro",
        "en": "Romania",
        "de": "Rumänien",
        "languages": [
            {
                "id": "ro",
                "origin": "română",
                "name": "Romanian"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 683506,
                "country_id": "ro",
                "origin": "Bucharest",
                "ascii": "Bucharest",
                "en": "Bucharest",
                "de": "Bukarest"
            }
        ]
    },
    {
        "id": "ru",
        "en": "Russian federation",
        "de": "Russland",
        "languages": [
            {
                "id": "ru",
                "origin": "Русский",
                "name": "Russian"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 472045,
                "country_id": "ru",
                "origin": "Voronezh",
                "ascii": "Voronezh",
                "en": "Voronezh",
                "de": "Woronesch"
            },
            {
                "id": 472757,
                "country_id": "ru",
                "origin": "Volgograd",
                "ascii": "Volgograd",
                "en": "Volgograd",
                "de": "Wolgograd"
            },
            {
                "id": 479561,
                "country_id": "ru",
                "origin": "Ufa",
                "ascii": "Ufa",
                "en": "Ufa",
                "de": "Ufa"
            },
            {
                "id": 498817,
                "country_id": "ru",
                "origin": "Saint Petersburg",
                "ascii": "Saint Petersburg",
                "en": "Saint Petersburg",
                "de": "Sankt Petersburg"
            },
            {
                "id": 499099,
                "country_id": "ru",
                "origin": "Samara",
                "ascii": "Samara",
                "en": "Samara",
                "de": "Samara"
            },
            {
                "id": 501175,
                "country_id": "ru",
                "origin": "Rostov-na-Donu",
                "ascii": "Rostov-na-Donu",
                "en": "Rostov-on-Don",
                "de": "Rostow am Don"
            },
            {
                "id": 520555,
                "country_id": "ru",
                "origin": "Nizhniy Novgorod",
                "ascii": "Nizhniy Novgorod",
                "en": "Nizhny Novgorod",
                "de": "Nischni Nowgorod"
            },
            {
                "id": 524901,
                "country_id": "ru",
                "origin": "Moscow",
                "ascii": "Moscow",
                "en": "Moscow",
                "de": "Moskau"
            },
            {
                "id": 551487,
                "country_id": "ru",
                "origin": "Kazan",
                "ascii": "Kazan",
                "en": "Kazan'",
                "de": "Kasan"
            },
            {
                "id": 1486209,
                "country_id": "ru",
                "origin": "Yekaterinburg",
                "ascii": "Yekaterinburg",
                "en": "Yekaterinburg",
                "de": "Jekaterinburg"
            },
            {
                "id": 1496153,
                "country_id": "ru",
                "origin": "Omsk",
                "ascii": "Omsk",
                "en": "Omsk",
                "de": "Omsk"
            },
            {
                "id": 1496747,
                "country_id": "ru",
                "origin": "Novosibirsk",
                "ascii": "Novosibirsk",
                "en": "Novosibirsk",
                "de": "Nowosibirsk"
            },
            {
                "id": 1502026,
                "country_id": "ru",
                "origin": "Krasnoyarsk",
                "ascii": "Krasnoyarsk",
                "en": "Krasnoyarsk",
                "de": "Krasnojarsk"
            },
            {
                "id": 1508291,
                "country_id": "ru",
                "origin": "Chelyabinsk",
                "ascii": "Chelyabinsk",
                "en": "Chelyabinsk",
                "de": "Tscheljabinsk"
            }
        ]
    },
    {
        "id": "rw",
        "en": "Rwanda",
        "de": "Ruanda",
        "languages": [
            {
                "id": "fr",
                "origin": "français, langue française",
                "name": "French"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 202061,
                "country_id": "rw",
                "origin": "Kigali",
                "ascii": "Kigali",
                "en": "Kigali",
                "de": "Kigali"
            }
        ]
    },
    {
        "id": "kn",
        "en": "Saint kitts and nevis",
        "de": "St. kitts und nevis",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "lc",
        "en": "Saint lucia",
        "de": "St. lucia",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "vc",
        "en": "Saint vincent and the grenadines",
        "de": "St. vincent und die grenadinen",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "ws",
        "en": "Samoa",
        "de": "Samoa",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "sm",
        "en": "San marino",
        "de": "San marino",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "st",
        "en": "Sao tome and principe",
        "de": "São tomé und príncipe",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "sa",
        "en": "Saudi arabia",
        "de": "Saudi-arabien",
        "languages": [
            {
                "id": "ar",
                "origin": "العربية",
                "name": "Arabic"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 104515,
                "country_id": "sa",
                "origin": "Mecca",
                "ascii": "Mecca",
                "en": "Makkah al Mukarramah",
                "de": "Mekka"
            },
            {
                "id": 108410,
                "country_id": "sa",
                "origin": "Riyadh",
                "ascii": "Riyadh",
                "en": "Riyadh",
                "de": "Riad"
            },
            {
                "id": 109223,
                "country_id": "sa",
                "origin": "Medina",
                "ascii": "Medina",
                "en": "Medina",
                "de": "Medina"
            },
            {
                "id": 110336,
                "country_id": "sa",
                "origin": "Dammam",
                "ascii": "Dammam",
                "en": "Dammam",
                "de": "Dammam"
            }
        ]
    },
    {
        "id": "sn",
        "en": "Senegal",
        "de": "Senegal",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2253354,
                "country_id": "sn",
                "origin": "Dakar",
                "ascii": "Dakar",
                "en": "Dakar",
                "de": "Dakar"
            }
        ]
    },
    {
        "id": "rs",
        "en": "Serbia",
        "de": "Serbien",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            },
            {
                "id": "hr",
                "origin": "hrvatski",
                "name": "Croatian"
            }
        ],
        "cities": [
            {
                "id": 792680,
                "country_id": "rs",
                "origin": "Belgrade",
                "ascii": "Belgrade",
                "en": "Belgrade",
                "de": "Belgrad"
            }
        ]
    },
    {
        "id": "sc",
        "en": "Seychelles",
        "de": "Seychellen",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "sl",
        "en": "Sierra leone",
        "de": "Sierra leone",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "sg",
        "en": "Singapore",
        "de": "Singapur",
        "languages": [
            {
                "id": "cn",
                "origin": null,
                "name": "Chinese (simplified)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1880252,
                "country_id": "sg",
                "origin": "Singapore",
                "ascii": "Singapore",
                "en": "Singapore",
                "de": "Singapur"
            }
        ]
    },
    {
        "id": "sk",
        "en": "Slovakia",
        "de": "Slowakei",
        "languages": [
            {
                "id": "sk",
                "origin": "slovenčina",
                "name": "Slovak"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "si",
        "en": "Slovenia",
        "de": "Slowenien",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "sb",
        "en": "Solomon islands",
        "de": "Salomonen",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "so",
        "en": "Somalia",
        "de": "Somalia",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 53654,
                "country_id": "so",
                "origin": "Mogadishu",
                "ascii": "Mogadishu",
                "en": "Mogadishu",
                "de": "Mogadischu"
            }
        ]
    },
    {
        "id": "za",
        "en": "South africa",
        "de": "Südafrika",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 964137,
                "country_id": "za",
                "origin": "Pretoria",
                "ascii": "Pretoria",
                "en": "Pretoria",
                "de": "Pretoria"
            },
            {
                "id": 993800,
                "country_id": "za",
                "origin": "Johannesburg",
                "ascii": "Johannesburg",
                "en": "Johannesburg",
                "de": "Johannesburg"
            },
            {
                "id": 1007311,
                "country_id": "za",
                "origin": "Durban",
                "ascii": "Durban",
                "en": "Durban",
                "de": "Durban"
            },
            {
                "id": 3369157,
                "country_id": "za",
                "origin": "Cape Town",
                "ascii": "Cape Town",
                "en": "Cape Town",
                "de": "Kapstadt"
            }
        ]
    },
    {
        "id": "ss",
        "en": "South sudan",
        "de": "Südsudan",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "es",
        "en": "Spain",
        "de": "Spanien",
        "languages": [
            {
                "id": "ct",
                "origin": null,
                "name": "Catalan"
            },
            {
                "id": "es",
                "origin": "español, castellano",
                "name": "Spanish"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3117735,
                "country_id": "es",
                "origin": "Madrid",
                "ascii": "Madrid",
                "en": "Madrid",
                "de": "Madrid"
            },
            {
                "id": 3128760,
                "country_id": "es",
                "origin": "Barcelona",
                "ascii": "Barcelona",
                "en": "Barcelona",
                "de": "Barcelona"
            }
        ]
    },
    {
        "id": "lk",
        "en": "Sri lanka",
        "de": "Sri lanka",
        "languages": [
            {
                "id": "si",
                "origin": "සිංහල",
                "name": "Sinhala"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "sd",
        "en": "Sudan",
        "de": "Sudan",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 379252,
                "country_id": "sd",
                "origin": "Khartoum",
                "ascii": "Khartoum",
                "en": "Khartoum",
                "de": "Khartum"
            }
        ]
    },
    {
        "id": "sr",
        "en": "Suriname",
        "de": "Suriname",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "sz",
        "en": "Eswatini",
        "de": "Eswatini",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "se",
        "en": "Sweden",
        "de": "Schweden",
        "languages": [
            {
                "id": "sv",
                "origin": "svenska",
                "name": "Swedish"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2673730,
                "country_id": "se",
                "origin": "Stockholm",
                "ascii": "Stockholm",
                "en": "Stockholm",
                "de": "Stockholm"
            }
        ]
    },
    {
        "id": "ch",
        "en": "Switzerland",
        "de": "Schweiz",
        "languages": [
            {
                "id": "de",
                "origin": "Deutsch",
                "name": "German"
            },
            {
                "id": "it",
                "origin": "Italiano",
                "name": "Italian"
            },
            {
                "id": "fr",
                "origin": "français, langue française",
                "name": "French"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "sy",
        "en": "Syrian arab republic",
        "de": "Syrien",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 170063,
                "country_id": "sy",
                "origin": "Aleppo",
                "ascii": "Aleppo",
                "en": "Aleppo",
                "de": "Aleppo"
            },
            {
                "id": 170654,
                "country_id": "sy",
                "origin": "Damascus",
                "ascii": "Damascus",
                "en": "Damascus",
                "de": "Damaskus"
            }
        ]
    },
    {
        "id": "tj",
        "en": "Tajikistan",
        "de": "Tadschikistan",
        "languages": [
            {
                "id": "tg",
                "origin": "тоҷикӣ, toğikī, تاجیکی‎",
                "name": "Tajik"
            }
        ],
        "cities": []
    },
    {
        "id": "tz",
        "en": "Tanzania, united republic of",
        "de": "Tansania",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 152224,
                "country_id": "tz",
                "origin": "Mwanza",
                "ascii": "Mwanza",
                "en": "Mwanza",
                "de": "Mwanza"
            },
            {
                "id": 160263,
                "country_id": "tz",
                "origin": "Dar es Salaam",
                "ascii": "Dar es Salaam",
                "en": "Dar es Salaam",
                "de": "Daressalam"
            }
        ]
    },
    {
        "id": "th",
        "en": "Thailand",
        "de": "Thailand",
        "languages": [
            {
                "id": "th",
                "origin": "ไทย",
                "name": "Thai"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1609350,
                "country_id": "th",
                "origin": "Bangkok",
                "ascii": "Bangkok",
                "en": "Bangkok",
                "de": "Bangkok"
            }
        ]
    },
    {
        "id": "tl",
        "en": "Timor-leste",
        "de": "Osttimor",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "tg",
        "en": "Togo",
        "de": "Togo",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "to",
        "en": "Tonga",
        "de": "Tonga",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "tt",
        "en": "Trinidad and tobago",
        "de": "Trinidad und tobago",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "tn",
        "en": "Tunisia",
        "de": "Tunesien",
        "languages": [
            {
                "id": "ar",
                "origin": "العربية",
                "name": "Arabic"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "tr",
        "en": "Türkiye",
        "de": "Türkei",
        "languages": [
            {
                "id": "tr",
                "origin": "Türkçe",
                "name": "Turkish"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 306571,
                "country_id": "tr",
                "origin": "Konya",
                "ascii": "Konya",
                "en": "Konya",
                "de": "Konya"
            },
            {
                "id": 308464,
                "country_id": "tr",
                "origin": "Kayseri",
                "ascii": "Kayseri",
                "en": "Kayseri",
                "de": "Kayseri"
            },
            {
                "id": 311046,
                "country_id": "tr",
                "origin": "İzmir",
                "ascii": "Izmir",
                "en": "Izmir",
                "de": "Izmir"
            },
            {
                "id": 314830,
                "country_id": "tr",
                "origin": "Gaziantep",
                "ascii": "Gaziantep",
                "en": "Gaziantep",
                "de": "Gaziantep"
            },
            {
                "id": 316541,
                "country_id": "tr",
                "origin": "Diyarbakır",
                "ascii": "Diyarbakir",
                "en": "Diyarbakir",
                "de": "Diyarbakır"
            },
            {
                "id": 323777,
                "country_id": "tr",
                "origin": "Antalya",
                "ascii": "Antalya",
                "en": "Antalya",
                "de": "Antalya"
            },
            {
                "id": 323786,
                "country_id": "tr",
                "origin": "Ankara",
                "ascii": "Ankara",
                "en": "Ankara",
                "de": "Ankara"
            },
            {
                "id": 325363,
                "country_id": "tr",
                "origin": "Adana",
                "ascii": "Adana",
                "en": "Adana",
                "de": "Adana"
            },
            {
                "id": 745044,
                "country_id": "tr",
                "origin": "Istanbul",
                "ascii": "Istanbul",
                "en": "Istanbul",
                "de": "Istanbul"
            },
            {
                "id": 750269,
                "country_id": "tr",
                "origin": "Bursa",
                "ascii": "Bursa",
                "en": "Bursa",
                "de": "Bursa"
            }
        ]
    },
    {
        "id": "tm",
        "en": "Turkmenistan",
        "de": "Turkmenistan",
        "languages": [
            {
                "id": "tk",
                "origin": "Türkmen, Түркмен",
                "name": "Turkmen"
            }
        ],
        "cities": []
    },
    {
        "id": "tv",
        "en": "Tuvalu",
        "de": "Tuvalu",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "ug",
        "en": "Uganda",
        "de": "Uganda",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 232422,
                "country_id": "ug",
                "origin": "Kampala",
                "ascii": "Kampala",
                "en": "Kampala",
                "de": "Kampala"
            }
        ]
    },
    {
        "id": "ua",
        "en": "Ukraine",
        "de": "Ukraine",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            },
            {
                "id": "uk",
                "origin": "українська",
                "name": "Ukrainian"
            }
        ],
        "cities": [
            {
                "id": 698740,
                "country_id": "ua",
                "origin": "Odesa",
                "ascii": "Odesa",
                "en": "Odesa",
                "de": "Odessa"
            },
            {
                "id": 703448,
                "country_id": "ua",
                "origin": "Kyiv",
                "ascii": "Kyiv",
                "en": "Kyiv",
                "de": "Kyiw"
            },
            {
                "id": 706483,
                "country_id": "ua",
                "origin": "Kharkiv",
                "ascii": "Kharkiv",
                "en": "Kharkiv",
                "de": "Charkiw"
            }
        ]
    },
    {
        "id": "ae",
        "en": "United arab emirates",
        "de": "Vereinigte arabische emirate",
        "languages": [
            {
                "id": "ar",
                "origin": "العربية",
                "name": "Arabic"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 292223,
                "country_id": "ae",
                "origin": "Dubai",
                "ascii": "Dubai",
                "en": "Dubai",
                "de": "Dubai"
            },
            {
                "id": 292672,
                "country_id": "ae",
                "origin": "Sharjah",
                "ascii": "Sharjah",
                "en": "Sharjah",
                "de": "Schardscha"
            },
            {
                "id": 292968,
                "country_id": "ae",
                "origin": "Abu Dhabi",
                "ascii": "Abu Dhabi",
                "en": "Abu Dhabi",
                "de": "Abu Dhabi"
            }
        ]
    },
    {
        "id": "gb",
        "en": "United kingdom of great britain and northern ireland",
        "de": "Vereinigtes königreich",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 2643743,
                "country_id": "gb",
                "origin": "London",
                "ascii": "London",
                "en": "London",
                "de": "London"
            },
            {
                "id": 2655603,
                "country_id": "gb",
                "origin": "Birmingham",
                "ascii": "Birmingham",
                "en": "Birmingham",
                "de": "Birmingham"
            }
        ]
    },
    {
        "id": "us",
        "en": "United states of america",
        "de": "Vereinigte staaten",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "us",
                "origin": null,
                "name": "English (US)"
            }
        ],
        "cities": [
            {
                "id": 4560349,
                "country_id": "us",
                "origin": "Philadelphia",
                "ascii": "Philadelphia",
                "en": "Philadelphia",
                "de": "Philadelphia"
            },
            {
                "id": 4684888,
                "country_id": "us",
                "origin": "Dallas",
                "ascii": "Dallas",
                "en": "Dallas",
                "de": "Dallas"
            },
            {
                "id": 4699066,
                "country_id": "us",
                "origin": "Houston",
                "ascii": "Houston",
                "en": "Houston",
                "de": "Houston"
            },
            {
                "id": 4726206,
                "country_id": "us",
                "origin": "San Antonio",
                "ascii": "San Antonio",
                "en": "San Antonio",
                "de": "San Antonio"
            },
            {
                "id": 4887398,
                "country_id": "us",
                "origin": "Chicago",
                "ascii": "Chicago",
                "en": "Chicago",
                "de": "Chicago"
            },
            {
                "id": 5110266,
                "country_id": "us",
                "origin": "The Bronx",
                "ascii": "The Bronx",
                "en": "The Bronx",
                "de": null
            },
            {
                "id": 5110302,
                "country_id": "us",
                "origin": "Brooklyn",
                "ascii": "Brooklyn",
                "en": "Brooklyn",
                "de": "Brooklyn"
            },
            {
                "id": 5125771,
                "country_id": "us",
                "origin": "Manhattan",
                "ascii": "Manhattan",
                "en": "Manhattan",
                "de": null
            },
            {
                "id": 5133273,
                "country_id": "us",
                "origin": "Queens",
                "ascii": "Queens",
                "en": "Borough of Queens",
                "de": null
            },
            {
                "id": 5308655,
                "country_id": "us",
                "origin": "Phoenix",
                "ascii": "Phoenix",
                "en": "Phoenix",
                "de": "Phoenix"
            },
            {
                "id": 5368361,
                "country_id": "us",
                "origin": "Los Angeles",
                "ascii": "Los Angeles",
                "en": "Los Angeles",
                "de": "Los Angeles"
            },
            {
                "id": 5391811,
                "country_id": "us",
                "origin": "San Diego",
                "ascii": "San Diego",
                "en": "San Diego",
                "de": "San Diego"
            },
            {
                "id": 5392171,
                "country_id": "us",
                "origin": "San Jose",
                "ascii": "San Jose",
                "en": "San Jose",
                "de": "San José"
            }
        ]
    },
    {
        "id": "uy",
        "en": "Uruguay",
        "de": "Uruguay",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3441575,
                "country_id": "uy",
                "origin": "Montevideo",
                "ascii": "Montevideo",
                "en": "Montevideo",
                "de": "Montevideo"
            }
        ]
    },
    {
        "id": "uz",
        "en": "Uzbekistan",
        "de": "Usbekistan",
        "languages": [
            {
                "id": "uz",
                "origin": "zbek, Ўзбек, أۇزبېك‎",
                "name": "Uzbek"
            }
        ],
        "cities": [
            {
                "id": 1512569,
                "country_id": "uz",
                "origin": "Tashkent",
                "ascii": "Tashkent",
                "en": "Tashkent",
                "de": "Taschkent"
            },
            {
                "id": 1513157,
                "country_id": "uz",
                "origin": "Namangan",
                "ascii": "Namangan",
                "en": "Namangan",
                "de": "Namangan"
            }
        ]
    },
    {
        "id": "vu",
        "en": "Vanuatu",
        "de": "Vanuatu",
        "languages": [
            {
                "id": "fr",
                "origin": "français, langue française",
                "name": "French"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": []
    },
    {
        "id": "ve",
        "en": "Venezuela (bolivarian republic of)",
        "de": "Venezuela",
        "languages": [
            {
                "id": "sp",
                "origin": null,
                "name": "Spanish (Latin America)"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 3625549,
                "country_id": "ve",
                "origin": "Valencia",
                "ascii": "Valencia",
                "en": "Valencia",
                "de": "Valencia"
            },
            {
                "id": 3632998,
                "country_id": "ve",
                "origin": "Maracay",
                "ascii": "Maracay",
                "en": "Maracay",
                "de": null
            },
            {
                "id": 3633009,
                "country_id": "ve",
                "origin": "Maracaibo",
                "ascii": "Maracaibo",
                "en": "Maracaibo",
                "de": "Maracaibo"
            },
            {
                "id": 3646738,
                "country_id": "ve",
                "origin": "Caracas",
                "ascii": "Caracas",
                "en": "Caracas",
                "de": "Caracas"
            },
            {
                "id": 3648522,
                "country_id": "ve",
                "origin": "Barquisimeto",
                "ascii": "Barquisimeto",
                "en": "Barquisimeto",
                "de": "Barquisimeto"
            }
        ]
    },
    {
        "id": "vn",
        "en": "Viet nam",
        "de": "Vietnam",
        "languages": [
            {
                "id": "vi",
                "origin": "Tiếng Việt",
                "name": "Vietnamese"
            },
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 1566083,
                "country_id": "vn",
                "origin": "Ho Chi Minh City",
                "ascii": "Ho Chi Minh City",
                "en": "Ho Chi Minh City",
                "de": "Ho-Chi-Minh-Stadt"
            },
            {
                "id": 1581130,
                "country_id": "vn",
                "origin": "Hanoi",
                "ascii": "Hanoi",
                "en": "Hanoi",
                "de": "Hanoi"
            }
        ]
    },
    {
        "id": "ye",
        "en": "Yemen",
        "de": "Jemen",
        "languages": [
            {
                "id": "ar",
                "origin": "العربية",
                "name": "Arabic"
            }
        ],
        "cities": [
            {
                "id": 71137,
                "country_id": "ye",
                "origin": "Sanaa",
                "ascii": "Sanaa",
                "en": "Sanaa",
                "de": "Sanaa"
            }
        ]
    },
    {
        "id": "zm",
        "en": "Zambia",
        "de": "Sambia",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 909137,
                "country_id": "zm",
                "origin": "Lusaka",
                "ascii": "Lusaka",
                "en": "Lusaka",
                "de": "Lusaka"
            }
        ]
    },
    {
        "id": "zw",
        "en": "Zimbabwe",
        "de": "Simbabwe",
        "languages": [
            {
                "id": "en",
                "origin": "English",
                "name": "English (International)"
            }
        ],
        "cities": [
            {
                "id": 890299,
                "country_id": "zw",
                "origin": "Harare",
                "ascii": "Harare",
                "en": "Harare",
                "de": "Harare"
            },
            {
                "id": 894701,
                "country_id": "zw",
                "origin": "Bulawayo",
                "ascii": "Bulawayo",
                "en": "Bulawayo",
                "de": "Bulawayo"
            }
        ]
    }
]
```
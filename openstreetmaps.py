import time
from collections import Counter
from typing import Optional

import requests
from requests.auth import HTTPProxyAuth
from unidecode import unidecode

from proxy import Proxy
from settings import Settings


class OSM:
    @classmethod
    def _request(
        cls,
        params: dict,
        proxies: Optional[dict] = None,
        auth: Optional[HTTPProxyAuth] = None,
    ) -> requests.Response:
        try:
            return requests.request(
                method="GET",
                url="http://overpass-api.de/api/interpreter",
                params=params,
                proxies=proxies,
                auth=auth,
            )
        except requests.exceptions.ProxyError as e:
            time.sleep(1)
            print(f"[OMS] Retry... Raise ProxyError: {str(e)}")
            cls._request(params, proxies, auth)

    @classmethod
    def request(cls, proxy: Proxy, params: dict) -> dict:
        while True:
            response = cls._request(params=params)
            if response.status_code != 429:
                break

            for proxies in proxy.proxies:
                response = cls._request(params=params, proxies=proxies, auth=proxy.auth)
                if response.status_code != 429:
                    break

            if response.status_code != 429:
                break

        print(f"[OMS] Received response: {response.json()}")
        return response.json()


class OSMCity(OSM):
    @classmethod
    def _template(cls, city: str, language: str = None):
        if language:
            name = f'"name:{language}"="{city}"'
        else:
            name = f'"name"="{city}"'

        return f"""[out:json];node[place~"^(city|town|village)$"][{name}];out body;"""

    @classmethod
    def get(cls, proxy: Proxy, city: dict) -> dict:
        names = dict(origin=city["origin"], ascii=city["ascii"])
        for language in Settings.AVAILABLE_LANGUAGES:
            names[language] = city[language]

        elements = list()

        for language in Settings.AVAILABLE_LANGUAGES:
            if names.get(language):
                response = cls.request(
                    proxy=proxy,
                    params=dict(
                        data=cls._template(city=names[language], language=language)
                    ),
                )
                if response.get("elements"):
                    elements = elements + response["elements"]

                response = cls.request(
                    proxy=proxy, params=dict(data=cls._template(city=names[language]))
                )
                if response.get("elements"):
                    elements = elements + response["elements"]

            response = cls.request(
                proxy=proxy,
                params=dict(data=cls._template(city=names["ascii"], language=language)),
            )
            if response.get("elements"):
                elements = elements + response["elements"]

            response = cls.request(
                proxy=proxy,
                params=dict(
                    data=cls._template(city=names["origin"], language=language)
                ),
            )
            if response.get("elements"):
                elements = elements + response["elements"]

        response = cls.request(
            proxy=proxy, params=dict(data=cls._template(city=names["ascii"]))
        )
        if response and response.get("elements"):
            elements = elements + response["elements"]

        response = cls.request(
            proxy=proxy, params=dict(data=cls._template(city=names["origin"]))
        )
        if response and response.get("elements"):
            elements = elements + response["elements"]

        tags = dict()
        for language in Settings.AVAILABLE_LANGUAGES:
            tags[language] = []

        for element in elements:
            for language in Settings.AVAILABLE_LANGUAGES:
                if element["tags"].get(f"name:{language}"):
                    if language == "en":
                        tags[language].append(
                            unidecode(element["tags"][f"name:{language}"])
                        )
                    else:
                        tags[language].append((element["tags"][f"name:{language}"]))
                if language == "en":
                    if element["tags"].get("name"):
                        tags["en"].append(unidecode(element["tags"]["name"]))

        updated_fields = dict()
        for language, names in tags.items():
            if tags.get(language):
                updated_fields[language] = Counter(names).most_common(1)[0][0]

        # Заполнение города дефолтом если ничего не найдено.
        if not updated_fields:
            if not city.get("en"):
                updated_fields["en"] = city["ascii"]

        if updated_fields:
            print(f"[OSM] City:{city} updated fields: {updated_fields}")
        else:
            print(f"[OSM] City:{city} not found information")

        return dict(id=city["id"], updated_fields=updated_fields)

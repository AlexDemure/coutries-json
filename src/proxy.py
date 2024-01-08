import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPProxyAuth

from src.core.settings import Settings


class _SSLProxyDeprecated:
    host: str = "https://www.sslproxies.org/"
    proxies: list[dict] = None

    def __init__(self) -> None:
        self.proxies = self.get()

    def refresh(self) -> None:
        self.proxies = self.get()

    @classmethod
    def get(cls) -> list[dict]:
        response = requests.get(cls.host)

        table = BeautifulSoup(response.content, "html.parser").find("table")

        table_columns = []
        table_content = []

        for tr in table.find_all("tr"):
            if tr.find_all("th"):
                table_columns = [tag.text for tag in tr.find_all("th")]

            if tr.find_all("td"):
                item = dict()

                for index, column in enumerate(table_columns):
                    item[column] = tr.find_all("td")[index].text

                table_content.append(item)

        proxies = [
            {
                "http:": f'http://{proxy["IP Address"]}:{proxy["Port"]}',
                "https": f'https://{proxy["IP Address"]}:{proxy["Port"]}',
            }
            for proxy in table_content
            if proxy["Https"] != "no"
        ]

        for proxy in proxies:
            try:
                response = requests.get("http://google.com", proxies=proxy)
                print(f"[Proxy] Connect success: {response.status_code}")
            except requests.exceptions.ConnectionError as e:
                print(f"[_SSLProxyDeprecated] Connect is failed: {e}")
                proxies.remove(proxy)

        return proxies


class Proxy:
    auth: HTTPProxyAuth = None
    proxies: list[dict] = None

    def __init__(self) -> None:
        self.auth = HTTPProxyAuth(Settings.PROXY_USERNAME, Settings.PROXY_PASSWORD)
        self.proxies = self.get()

    @classmethod
    def get(cls) -> list[dict]:
        proxies = [
            {"http": f"http://{proxy}", "https": f"https://{proxy}"}
            for proxy in Settings.PROXY_HOSTS
        ]

        for proxy in proxies:
            try:
                response = requests.get(
                    "http://google.com",
                    proxies=proxy,
                    auth=HTTPProxyAuth(
                        Settings.PROXY_USERNAME, Settings.PROXY_PASSWORD
                    ),
                )
                print(f"[Proxy] Connect success: {response.status_code}")
            except requests.exceptions.ConnectionError as e:
                print(f"[Proxy] Connect is failed: {e}")
                raise e

        return proxies

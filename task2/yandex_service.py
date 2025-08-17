import requests
from requests import Response


class YandexAPI:

    api_root: str = r'https://cloud-api.yandex.net/v1/disk/resources'

    def __init__(self, token: str):
        self.token = token
    
    def create_dir(self, dirname: str) -> Response:
        headers = self.get_headers()
        params = {
            'path': f'/{dirname}'
        }
        return requests.put(self.api_root, headers=headers, params=params)

    def get_headers(self):
        return {
            'Authorization': f'OAuth {self.token}'
        }

import os
import unittest
import requests
from dotenv import load_dotenv

from yandex_service import YandexAPI

load_dotenv()


class TestYandexAPIIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        token = os.getenv('YANDEX_TOKEN')
        if not token:
            raise RuntimeError('Установите переменную окружения YANDEX_TOKEN с OAuth токеном Яндекс.Диска')
        cls.client = YandexAPI(token)
    
    def tearDown(self):
        dirname = 'test_api_folder'
        url = f'{self.client.api_root}'
        params = {'path': f'/{dirname}'}
        requests.delete(url, headers=self.client.get_headers(), params=params)

    def test_create_dir_success(self):
        dirname = 'test_api_folder'
        response = self.client.create_dir(dirname)
        self.assertIn(response.status_code, (201, 409))

        url = f'{self.client.api_root}'
        params = {'path': f'/{dirname}'}
        check = requests.get(url, headers=self.client.get_headers(), params=params)

        self.assertEqual(check.status_code, 200)
        self.assertEqual(check.json()['type'], 'dir')
        self.assertEqual(check.json()['name'], dirname)

    def test_create_dir_unauthorized(self):
        bad_client = YandexAPI('fake_token')
        response = bad_client.create_dir('unauth_folder')
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()

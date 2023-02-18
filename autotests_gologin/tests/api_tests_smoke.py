import logging
import configurator
import allure
import pytest
import requests
import random
import string
from resources import smoke_tests_requests


class TestC1Pages:
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()

    test_data = {
        "user": {
            "login": configurator.LOGIN,
            "password": configurator.PASSWORD,
            "token": configurator.ACCESS_TOKEN_1,

        }

    }

    @allure.description('Позитивный тест проверки страниц Tradernet')
    @allure.severity('normal')
    # метод для получения данных перед выполнением тестов
    def setup_class(self):

        try:
            self.test_data['user1'] = smoke_tests_requests.get_user_info(self.test_data['user']['token'])
            self.test_data['user1'] = self.test_data['user1'].json()['_id']
            print(self.test_data['user1'])

            def generate_name(prefix='testprofile+'):
                random_part = ''.join(random.choice(string.ascii_lowercase + string.digits)
                                      for _ in range(10))

                return prefix + random_part

            self.test_data['name'] = generate_name()
        except Exception as e:
            pytest.exit(e)
        else:
            self.logger.info('Precondition successful!')

    def test_1_user_info(self):
        with allure.step('Метод отдает инфо по user'):
            response = smoke_tests_requests.get_user_info(self.test_data['user']['token'])
            assert response.status_code == requests.codes.ok
            assert response.json()['_id'] == '63ee5f144b61f6ecb78b9681'
            assert response.json()['email'] == 'testgologin@yopmail.com'
            assert response.json()['isEmailConfirmed'] is not None
            assert response.json()['createdAt']
            assert response.json()['subscription']
            print(response.json())

    def test_2_profile_info(self):
        with allure.step('Метод отдает инфо по профилю'):
            response = smoke_tests_requests.get_profiles_info(self.test_data['user']['token'])
            assert response.status_code == requests.codes.ok
            for item in response.json()['profiles']:
                assert item['name']
                assert item['role']
                assert item['id']
            print(response.json())

    def test_3_create_profile(self):
        with allure.step('Метод создает профиль'):
            self.test_data['profile'] = smoke_tests_requests.post_create_profile(self.test_data['user']['token'],
                                                                                 name=self.test_data['name'])
            assert self.test_data['profile'].json()['name']
            assert self.test_data['profile'].json()['role']
            self.test_data['ID'] = self.test_data['profile'].json()['id']
            print(self.test_data['profile'].json())

    def test_4_delete_profiles(self):
        with allure.step('Метод удаляет профили'):
            response = smoke_tests_requests.delete_profile(self.test_data['user']['token'],
                                                           profile_id=self.test_data['ID'])
            assert response.status_code == 204
            print(response)

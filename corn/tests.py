from rest_framework.test import APITestCase, APIClient
from . import models, serializers
from django.contrib.auth.models import User


class TestWeb(APITestCase):
    @classmethod
    def setUpClass(cls):
        cls.cls_atomics = cls._enter_atomics()
        cls.client = APIClient()
        cls.username = 'TestUsername'
        cls.password = 'TestPassword'
        cls.email = 'TestEmail@google.com'
        cls.create_user_data = {"username": cls.username, 'email': cls.email, 'password': cls.password}
    # def setUp(self) -> None:
    #     self.configuration = models.Configurations.objects.create(
    #         host=self.configuration_host,
    #         name=self.configuration_name,
    #         region_name=self.region_name
    #     )

    def test_01_create_user(self, expected_status_code=201):
        response = self.client.post('/api/auth/sign-up/', data=self.create_user_data)
        expected_result = {
            'id': 1,
            'username': self.username,
            'email': self.email,
            'password': "*****"
        }
        assert response.status_code == expected_status_code, \
            f"Actual status code - {response.status_code} " \
            f"is not equal to expected - {expected_status_code}"

        assert response.json() == expected_result, f"Actual result - " \
            f"{response.json()}, is not equal to expected - {expected_result}"

    def test_02_create_user_duplicate(self, expected_status_code=400):
        User.objects.create(username=self.username, email=self.email, password=self.password)
        response = self.client.post('/api/auth/sign-up/', data=self.create_user_data)
        expected_result = {"username": ["A user with that username already exists."]}
        assert response.status_code == expected_status_code, \
            f"Actual status code - {response.status_code} " \
            f"is not equal to expected - {expected_status_code}"
        assert response.json() == expected_result, f"Actual result - " \
            f"{response.json()}, is not equal to expected - {expected_result}"

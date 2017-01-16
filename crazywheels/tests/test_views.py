from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from factory import build as factory_build

from .factories import MessageFactory
from crazywheels.serializers import MessageSerializer

import pytest


class MessageApiTests(APITestCase):

    def setUp(self):
        self.api_data = factory_build(dict, FACTORY_CLASS=MessageFactory)

    @pytest.mark.django_db
    def test_message_create(self):
        api_url = reverse('message-list')
        api_response = self.client.post(api_url, data=self.api_data)
        self.assertEqual(api_response.status_code, HTTP_201_CREATED)

    @pytest.mark.django_db
    def test_message_list(self):
        api_url = reverse('message-list')
        api_response = self.client.get(api_url)
        self.assertEqual(api_response.status_code, HTTP_200_OK)

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK

from .factories import MessageFactory
from crazywheels.serializers import MessageSerializer

import pytest


class MessageApiTests(APITestCase):

    @pytest.mark.django_db
    def test_message_list(self):
        api_url = reverse('message-list')
        api_response = self.client.get(api_url)
        self.assertEqual(api_response.status_code, HTTP_200_OK)

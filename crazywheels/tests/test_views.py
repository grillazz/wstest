from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from factory import build as factory_build

from .factories import MessageFactory, MessageModel


class MessageApiTests(APITestCase):
    def setUp(self):
        self.api_data = factory_build(dict, FACTORY_CLASS=MessageFactory)
        self.api_url = reverse('message-list')

    def test_message_create(self):
        api_response = self.client.post(self.api_url, self.api_data, format='json')
        self.assertEqual(api_response.status_code, HTTP_201_CREATED)
        self.assertEqual(MessageModel.objects.count(), 1)
        self.assertEqual(MessageModel.objects.get().title, 'New Message for JJ')

    def test_message_list(self):
        api_response = self.client.get(self.api_url)
        self.assertEqual(api_response.status_code, HTTP_200_OK)

    def test_message_get(self):
        self.test_message_create()
        api_response = self.client.get('/api/v1/message/1/')
        self.assertEqual(api_response.status_code, HTTP_200_OK)
        self.assertEqual(api_response.data,
                         {'image': None, 'message': 'How are you Dude?', 'title': 'New Message for JJ'})



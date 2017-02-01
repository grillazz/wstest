from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from factory import build as factory_build

from .factories import MessageFactory, MessageModel


class MessageApiTests(APITestCase):
    def setUp(self):
        self.api_data = factory_build(dict, FACTORY_CLASS=MessageFactory)
        self.api_url = reverse('message-list')

    def create_message(self):
        return self.client.post(self.api_url, self.api_data, format='json')

    def test_message_create(self):
        api_response = self.create_message()
        self.assertEqual(api_response.status_code, HTTP_201_CREATED)
        self.assertEqual(MessageModel.objects.count(), 1)
        self.assertEqual(MessageModel.objects.get().title, 'New Message for JJ')

    def test_message_list(self):
        self.create_message()
        api_response = self.client.get(self.api_url)
        self.assertEqual(api_response.status_code, HTTP_200_OK)

    # def test_message_get(self):
    #     self.create_message()
    #     api_response = self.client.get('/api/v1/message/1/')
    #     self.assertEqual(api_response.status_code, HTTP_200_OK)
    #     self.assertEqual(api_response.data,
    #                      {'image': None, 'message': 'How are you Dude?', 'title': 'New Message for JJ'})

    def test_message_detail(self):
        self.create_message()
        created_message = MessageModel.objects.get()
        api_response = self.client.get(
            reverse('message-detail', kwargs={'pk': created_message.pk})
        )
        self.assertEqual(api_response.status_code, HTTP_200_OK)
        self.assertEqual(api_response.data['title'], self.api_data['title'])
        self.assertEqual(api_response.data['message'], self.api_data['message'])

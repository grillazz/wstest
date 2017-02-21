from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from rest_framework_jwt import utils

from .factories import MessageFactory, MessageModel, UserFactory

from ..serializers import MessageSerializer


class MessageApiTests(APITestCase):
    def setUp(self):
        self.csrf_client = APIClient(enforce_csrf_checks=False)
        self.user = UserFactory()
        self.message = MessageFactory.build()
        self.message_data = MessageSerializer(self.message).data
        self.message_url = reverse('message-list')
        self.jwt_url = reverse('api-token-auth')

        self.user_data = {
            'username': self.user.username,
            'password': UserFactory.DEFAULT_PASSWORD
        }
        self.token = self.csrf_client.post(self.jwt_url, self.user_data, format='json')
        self.token = self.token.data['token']


    def test_123(self):
        response = self.csrf_client.post(self.jwt_url, self.user_data, format='json')
        decoded_payload = utils.jwt_decode_handler(response.data['token'])
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(decoded_payload['username'], self.user.username)
        self.csrf_client.credentials(HTTP_AUTHORIZATION='JWT ' + response.data['token'])
        print("Authorization: JWT " + response.data['token'])
        api_response = self.csrf_client.get(self.message_url)
        self.assertEqual(api_response.status_code, HTTP_200_OK)
        pass


    #     def test_jwt_login_custom_response_json(self):
    #         """
    #         Ensure JWT login view using JSON POST works.
    #         """
    #         client = APIClient(enforce_csrf_checks=True)
    #
    #         response = client.post('/auth-token/', self.data, format='json')
    #
    #         decoded_payload = utils.jwt_decode_handler(response.data['token'])
    #
    #         self.assertEqual(response.status_code, status.HTTP_200_OK)
    #         self.assertEqual(decoded_payload['username'], self.username)
    #
    # self.assertEqual(response.data['user'], self.username)

    # def create_message(self):
    #     response = self.client.post(self.jwt_url, self.user_data, format='json')
    #     print(response.data['token'])
    #     self.client.credentials(HTTP_AUTHORIZATION='Authorization: JWT ' + response.data['token'])
    #     return self.client.post(self.message_url, self.message_data, format='json')
    #
    # def test_message_create(self):
    #     api_response = self.create_message()
    #     self.assertEqual(api_response.status_code, HTTP_201_CREATED)
    #     self.assertEqual(MessageModel.objects.count(), 1)
    #     self.assertEqual(MessageModel.objects.get().title, 'New Message for JJ')

    # def test_message_list(self):
    #      = self.client.post(self.jwt_url, self.user_data, format='json')
    #     header = {'HTTP_AUTHORIZATION': 'Authorization: JWT {}'.format(response.data['token'])}
    #     api_response = self.client.get(self.message_url, {}, **header)
    #     self.assertEqual(api_response.status_code, HTTP_200_OK)

    # def test_authorization(self):
    #     header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
    #     response = self.client.get(reverse('bookmark-list'), {}, **header)
    #     self.assertEqual(response.status_code, 200, "REST token-auth failed")

    #
    # def test_message_get(self):
    #     self.create_message()
    #     api_response = self.client.get('/api/v1/message/1/')
    #     self.assertEqual(api_response.status_code, HTTP_200_OK)
    #     self.assertEqual(api_response.data,
    #                      {'image': None, 'message': 'How are you Dude?', 'title': 'New Message for JJ'})
    #
    # def test_message_detail(self):
    #     self.create_message()
    #     created_message = MessageModel.objects.get()
    #     api_response = self.client.get(
    #         reverse('message-detail', kwargs={'pk': created_message.pk})
    #     )
    #     self.assertEqual(api_response.status_code, HTTP_200_OK)
    #     self.assertEqual(api_response.data['title'], self.message_data['title'])
    #     self.assertEqual(api_response.data['message'], self.message_data['message'])

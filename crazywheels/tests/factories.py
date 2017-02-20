from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

import factory
from faker import Faker

from crazywheels.models import MessageModel


class UserFactory(factory.django.DjangoModelFactory):
    DEFAULT_PASSWORD = 'very_dangerous_password'

    class Meta:
        model = get_user_model()
        exclude = ('DEFAULT_PASSWORD',)

    username = factory.LazyFunction(lambda: 'admin-%s' % Faker().uuid4())
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')

    @factory.lazy_attribute
    def password(self):
        """
        http://stackoverflow.com/questions/24748222/django-python-django-login-test-failed-with-factory-boy-and-authtools
        """
        return make_password(self.DEFAULT_PASSWORD)


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MessageModel

    title = "New Message for JJ"
    message = "How are you Dude?"
    # image = ImageField(filename='test.png')

from factory.django import DjangoModelFactory, ImageField

from crazywheels.models import MessageModel


class MessageFactory(DjangoModelFactory):
    class Meta:
        model = MessageModel

    title = "New Message for JJ"
    message = "How are you Dude?"
    # image = ImageField(filename='test.png')

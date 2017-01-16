from .models import MessageModel

from rest_framework.serializers import ModelSerializer


class MessageSerializer(ModelSerializer):

    class Meta:
        model = MessageModel
        fields = (
            'title',
            'message',
            'image'
        )

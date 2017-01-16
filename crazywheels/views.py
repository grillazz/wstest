from rest_framework.viewsets import ModelViewSet

from .models import MessageModel
from .serializers import MessageSerializer


class MessageViewSet(ModelViewSet):
    """ViewSet for the Message class"""

    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer

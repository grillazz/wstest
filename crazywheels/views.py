from django.views.generic.base import TemplateView

from rest_framework.viewsets import ModelViewSet

from .models import MessageModel
from .serializers import MessageSerializer


# REsT API endpoint views
class MessageViewSet(ModelViewSet):
    """ViewSet for the Message class"""

    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer


# Application AJAX views
class AjaxListMessagesView(TemplateView):

    template_name = "crazywheels/list_messages.html"

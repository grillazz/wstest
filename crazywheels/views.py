from django.views.generic.base import TemplateView

from rest_framework.viewsets import ModelViewSet

from .models import MessageModel
from .serializers import MessageSerializer

from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# REsT API endpoint views
class MessageViewSet(ModelViewSet):
    """ViewSet for the Message class"""
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer


# Application AJAX views
class AjaxListMessagesView(TemplateView):

    template_name = "crazywheels/list_messages.html"

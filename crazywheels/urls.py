from django.conf.urls import url, include
from rest_framework import routers

from .views import MessageViewSet, AjaxListMessagesView


router = routers.DefaultRouter()
router.register(r'message', MessageViewSet, base_name='message')

urlpatterns = (
    # urls for Django Rest Framework API
    url(r'api/v1/', include(router.urls)),
    url(r'crazywheels/list', AjaxListMessagesView.as_view(), name='crazywheels-list')

)

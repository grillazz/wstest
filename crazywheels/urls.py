from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from .views import MessageViewSet, AjaxListMessagesView


router = routers.DefaultRouter()
router.register(r'message', MessageViewSet, base_name='message')

urlpatterns = (
    # urls for Django Rest Framework API
    url(r'api/v1/', include(router.urls)),
    url(r'api/v1/api-token-auth/', obtain_jwt_token),
    url(r'crazywheels/list', AjaxListMessagesView.as_view(), name='crazywheels-list')

)

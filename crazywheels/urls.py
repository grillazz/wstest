from django.conf.urls import url, include
from rest_framework import routers

from .views import MessageViewSet


router = routers.DefaultRouter()
router.register(r'message', MessageViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    url(r'v1/', include(router.urls)),
)

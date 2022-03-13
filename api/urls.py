from django.urls import path,include
from rest_framework import routers,views

from . import views

router = routers.DefaultRouter()
router.register('User',views.UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
]

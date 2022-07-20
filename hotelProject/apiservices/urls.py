# basic URL config.
from django.urls import include, path
# importing routers
from rest_framework import routers
from .views import *

# define the router
router = routers.DefaultRouter()
# define the router path and viewset to be used
router.register(r'allServices', ServicesViewSet, basename='allServices')


# specify URL Path for rest_framework

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from .views import getview
from roomManager import views as viewsroom

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.http import HttpResponse,HttpRequest

urlpatterns = [
    path('roomavailability', getview, name='roomavailability'),
    path('demodata/inforoom/', viewsroom.info),
    path('demodata/room/', viewsroom.room),
]

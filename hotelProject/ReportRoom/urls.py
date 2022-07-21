from django.urls import path
from .views import *

urlpatterns = [
    path('information', roomlist.as_view(), name='roomlist'),
]


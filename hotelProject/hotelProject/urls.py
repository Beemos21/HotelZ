"""hotelProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('booking/', include('booking.urls')),
    # path('roomManager/', include('roomManager.urls')),

    path('api/authentication/', include('apiauthentication.urls'), name='apiauthentication'),
    path('api/reviews/', include('apireviews.urls'), name='apireviews'),
    path('api/branches/', include('apibranches.urls'), name='apibranches'),
    path('api/services/', include('apiservices.urls'), name='apiservices'),
    path('reportBooking/', include('reportBooking.urls'), name='reportBooking'),
    path('booking/', include('booking.urls'), name='booking'),
    path('roomManager/', include('roomManager.urls'), name='roomManager'),
]

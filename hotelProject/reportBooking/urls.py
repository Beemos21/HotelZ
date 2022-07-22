from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('checkin', TodayCheckin.as_view(), name='checkin'),
    path('checkout', TodayCheckout.as_view(), name='checkout'),
    path('CurrentVisitor', CurrentVisitor.as_view(), name='checkout'),
    path('AllVisitor', AllVisitor.as_view(), name='checkout'),
    path('test', test_pdf),
    path('roomAvailabilityForm/', views.searchForRoomAvailabilityViews, name="roomAvailabilityForm"),

]

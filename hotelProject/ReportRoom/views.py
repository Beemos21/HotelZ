from django.contrib.auth.mixins import LoginRequiredMixin
from wkhtmltopdf.views import PDFTemplateView
from .models import *
from django.conf import settings

from datetime import datetime
from django.db import connection

import random

from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker, Factory
import factory
from django_renderpdf.views import PDFView
# Create your views here.
from rest_framework import viewsets


from .models import *

from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.authentication import JWTAuthentication
from templates import *


class roomlist(LoginRequiredMixin, PDFView):
    template_name = 'reportroom\RoomTypeList.html'

    def get_context_data(self, *args,  **kwargs):

        sql1 = "SELECT roomManager_roomtype.id,roomManager_roomtype.capacity,roomManager_roomtype.type_name," \
               "roomManager_roomtype.price_per_day ,roomManager_roomtype.area,"\
                "roomManager_roomtype.bedType,"\
                "count(roomManager_room.id) as countofroom FROM roomManager_room " \
               "INNER JOIN roomManager_roomtype on roomManager_room.rtype_id = roomManager_roomtype.id  INNER JOIN " \
               "roomManager_availability_room on roomManager_room.id = roomManager_availability_room.room_id " \
               "GROUP BY roomManager_roomtype.id, roomManager_roomtype.capacity, " \
               "roomManager_roomtype.type_name,roomManager_roomtype.price_per_day "

        context = super().get_context_data(*args, **kwargs)
        roomslist = []
        with connection.cursor() as cursor:
            cursor.execute(sql1)
            rows = cursor.fetchall()

            for row in rows:
                room1 = {
                    'id': row[0],
                    'type_name': row[2],
                    'bedType': row[5],
                    'area': row[4],
                    'capacity': row[1],
                    'price_per_day': row[3],
                    'countofroom': row[6],
                }
                roomslist.append(room1)
        context['room'] = roomslist
        return context

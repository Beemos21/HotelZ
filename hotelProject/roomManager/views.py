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

# Create your views here.
from rest_framework import viewsets


from .models import *

from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.authentication import JWTAuthentication

def info(request):

    fake = Factory.create()

    class CityFactory(factory.Factory):
        class Meta:
            model = City

        city_name = factory.LazyAttribute(lambda _: fake.city())

    class HotelInfoFactory(factory.Factory):
        class Meta:
            model = HotelInfo

        name = factory.LazyAttribute(lambda _: fake.name())
        email = factory.LazyAttribute(lambda _: fake.ascii_company_email())
        reg_number = factory.LazyAttribute(lambda _: fake.random.randint(1, 999999))
        owner_name = factory.LazyAttribute(lambda _: fake.company())
        address = factory.LazyAttribute(lambda _: fake.address())
        city = factory.SubFactory(CityFactory)
        state = factory.LazyAttribute(lambda _: fake.state())
        phone = factory.LazyAttribute(lambda _: fake.phone_number())

    class RoomStatusFactory(factory.Factory):
        class Meta:
            model = RoomStatus

        roomstatus = factory.LazyAttribute(lambda _: fake.name())
        description = factory.LazyAttribute(lambda _: fake.name())

    class ServiceFactory(factory.Factory):
        class Meta:
            model = Service

        name = factory.LazyAttribute(lambda _: fake.name())
        name_ar = factory.LazyAttribute(lambda _: fake.name())
        price = factory.LazyAttribute(lambda _: fake.random.random())
        description = factory.LazyAttribute(lambda _: fake.text())

    class RoomTypeFactory(factory.Factory):
        class Meta:
            model = RoomType

        type_name = factory.LazyAttribute(
            lambda _: fake.random.choice(['Single room', 'Twin room', 'Double room',
                        'Triple room', 'Quad room', 'Double-Double room',
                     'Queen room', 'King room', 'Suite', 'Presidential suite', 'Studio', 'Connecting rooms']))

        type_name_ar = factory.LazyAttribute(
            lambda _: fake.random.choice(['???????? ??????????', '???????? ????????','???????? ???????????? ',
                 '???????? ????????????', '???????? ????????????','?????????? ???????????? ????????????', '???????? ????????????','????????' ,
                '???????? ???????????? | ???????????? ??????????????', '??????????????????',
                 '?????????? ??????????????','???????? ????????' ]))

        area = factory.LazyAttribute(lambda _: fake.random.randint(10, 50))
        bedType = factory.LazyAttribute(
            lambda _: fake.random.choice(['1 double bed', '2 single beds', '1 Sofa and 1 single bed']))

        bedType_ar = factory.LazyAttribute(
            lambda _: fake.random.choice(['???????? ????????????',
                  '1 ???????? ???????????? ?? 1 ???????? ??????????',
                  '2 ???????? ???????? ????????', '1 ???????? ?????????? 1 ???????? ???????? ????????', ' ???????? ???????? ????????????', ]))

        description = factory.LazyAttribute(lambda _: fake.name())
        capacity = factory.LazyAttribute(lambda _: fake.random.randint(1, 6))
        price_per_day = factory.LazyAttribute(lambda _: fake.random.random())

    for _ in range(5):
        city = CityFactory()
        city.save()
        hotel = HotelInfoFactory()
        count = City.objects.count()
        city = City.objects.all()[random.randint(0, count - 1)]  # single random object
        hotel.city = city
        hotel.save()
        service = ServiceFactory()
        service.save()
        status = RoomStatusFactory()
        type = RoomTypeFactory()
        status.save()
        type.save()

        count = RoomStatus.objects.count()
        status = RoomStatus.objects.all()[random.randint(0, count - 1)]
        count = RoomType.objects.count()
        type = RoomType.objects.all()[random.randint(0, count - 1)]
        count = HotelInfo.objects.count()
        hotel = HotelInfo.objects.all()[random.randint(0, count - 1)]


    return HttpResponse('creative')



def room(request):
    fake = Factory.create()

    class RoomFactory(factory.Factory):
        class Meta:
            model = Room

        title = factory.LazyAttribute(lambda _: fake.name())
        is_active = factory.LazyAttribute(lambda _: fake.boolean())
        rfloor = factory.LazyAttribute(lambda _: fake.random.randint(1, 50))
        cover_image = "mays/qr_code-mays_AzQ2wL4.png"
        featured = factory.LazyAttribute(lambda _: fake.boolean())
        #room_status = 1
        #hotel = 1

    class AvailabilityFactory(factory.Factory):
        class Meta:
            model = Availability_Room

        room = factory.SubFactory(RoomFactory)
        d1 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d2 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d3 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d4 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d5 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d6 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d7 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d8 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d9 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d10 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d11 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d12 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d13 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d14 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d15 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d16 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d17 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d18 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d19 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d20 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d21 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d22 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d23 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d24 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d25 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d26 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d27 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d28 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d29 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d30 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d31 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d32 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d33 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d34 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d35 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d36 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d37 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d38 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d39 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d40 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d41 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d42 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d43 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d44 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d45 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d46 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d47 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d48 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d49 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d50 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d51 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d52 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d53 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d54 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d55 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d56 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d57 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d58 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d59 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d60 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d61 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d62 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d63 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d64 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d65 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d66 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d67 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d68 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d69 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d70 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d71 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d72 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d73 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d74 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d75 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d76 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d77 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d78 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d79 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d80 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d81 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d82 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d83 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d84 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d85 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d86 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d87 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d88 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d89 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d90 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d91 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d92 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d93 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d94 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d95 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d96 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d97 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d98 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d99 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d100 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d101 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d102 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d103 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d104 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d105 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d106 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d107 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d108 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d109 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d110 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d111 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d112 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d113 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d114 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d115 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d116 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d117 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d118 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d119 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d120 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d121 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d122 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d123 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d124 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d125 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d126 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d127 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d128 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d129 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d130 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d131 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d132 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d133 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d134 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d135 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d136 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d137 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d138 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d139 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d140 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d141 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d142 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d143 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d144 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d145 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d146 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d147 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d148 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d149 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d150 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d151 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d152 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d153 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d154 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d155 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d156 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d157 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d158 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d159 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d160 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d161 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d162 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d163 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d164 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d165 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d166 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d167 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d168 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d169 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d170 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d171 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d172 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d173 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d174 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d175 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d176 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d177 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d178 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d179 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d180 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d181 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d182 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d183 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d184 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d185 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d186 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d187 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d188 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d189 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d190 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d191 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d192 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d193 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d194 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d195 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d196 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d197 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d198 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d199 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d200 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d201 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d202 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d203 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d204 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d205 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d206 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d207 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d208 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d209 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d210 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d211 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d212 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d213 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d214 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d215 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d216 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d217 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d218 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d219 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d220 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d221 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d222 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d223 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d224 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d225 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d226 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d227 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d228 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d229 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d230 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d231 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d232 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d233 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d234 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d235 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d236 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d237 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d238 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d239 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d240 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d241 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d242 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d243 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d244 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d245 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d246 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d247 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d248 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d249 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d250 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d251 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d252 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d253 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d254 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d255 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d256 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d257 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d258 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d259 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d260 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d261 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d262 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d263 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d264 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d265 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d266 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d267 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d268 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d269 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d270 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d271 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d272 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d273 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d274 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d275 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d276 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d277 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d278 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d279 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d280 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d281 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d282 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d283 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d284 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d285 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d286 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d287 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d288 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d289 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d290 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d291 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d292 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d293 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d294 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d295 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d296 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d297 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d298 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d299 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d300 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d301 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d302 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d303 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d304 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d305 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d306 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d307 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d308 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d309 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d310 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d311 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d312 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d313 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d314 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d315 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d316 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d317 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d318 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d319 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d320 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d321 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d322 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d323 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d324 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d325 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d326 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d327 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d328 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d329 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d330 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d331 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d332 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d333 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d334 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d335 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d336 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d337 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d338 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d339 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d340 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d341 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d342 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d343 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d344 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d345 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d346 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d347 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d348 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d349 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d350 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d351 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d352 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d353 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d354 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d355 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d356 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d357 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d358 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d359 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d360 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d361 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d362 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d363 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d364 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d365 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))
        d366 = factory.LazyAttribute(lambda _: fake.random.randint(0, 1))

    class RoomDisplayImagesFactory(factory.Factory):
        class Meta:
            model = RoomDisplayImages

        room = factory.SubFactory(RoomFactory)
        display_images = "mays/qr_code-mays_AzQ2wL4.png"

    for _ in range(5):
        room = RoomFactory()
        count = RoomStatus.objects.count()
        status = RoomStatus.objects.all()[random.randint(0, count - 1)]
        count = RoomType.objects.count()
        type = RoomType.objects.all()[random.randint(0, count - 1)]
        count = HotelInfo.objects.count()
        hotel = HotelInfo.objects.all()[random.randint(0, count - 1)]
        room.hotel = hotel
        room.room_status = status
        room.rtype = type
        room.save()

        count = Room.objects.count()
        room = Room.objects.all()[random.randint(0, count - 1)]
        display = RoomDisplayImagesFactory()
        display.room = room
        display.save()

        count = Room.objects.count()
        room = Room.objects.all()[random.randint(0, count - 1)]
        availability = AvailabilityFactory()
        availability.room = room
        availability.save()

    return HttpResponse('creative')

class GetRoom(PDFTemplateView):
    def get_context_data(self, **kwargs):
        context = super(GetRoom, self).get_context_data(**kwargs)
        rooms = Room.objects.all()
        # template_path = 'pdfReport.html'
        # print(settings.TEMPLATE_DIR)
        context = {
            'datatoshow': rooms,
            'hostname': settings.HOSTNAME,

        }
        return context


def getwhereofAvalabilitydays( fromdate, todate):
    fromdateasdate = datetime.datetime.strptime(fromdate, '%Y-%m-%d')
    fromdateasint = int(fromdateasdate.strftime('%j'))

    todateasdate = datetime.datetime.strptime(todate, '%Y-%m-%d')
    todateasint = int(todateasdate.strftime('%j'))

    toreturnstr = ""
    if todateasint >= fromdateasint:
        for i in range(fromdateasint, todateasint + 1):
            toreturnstr = toreturnstr + "d" + str(i) + "=0"
            if i == todateasint:
                continue
            toreturnstr = toreturnstr + " and "
    else:
        intermediate_str = str(fromdateasdate.year) + str("-12-31")
        intermediatedate = datetime.datetime.strptime(intermediate_str, '%Y-%m-%d')

        intermediateasint = int(intermediatedate.strftime('%j'))

        for i in range(fromdateasint, intermediateasint + 1):
            toreturnstr = toreturnstr + "d" + str(i) + "=0"
            # if i==intermediateasint :
            #     continue
            toreturnstr = toreturnstr + " and "

        # toreturnstr= toreturnstr + " and "

        for i in range(1, todateasint + 1):
            toreturnstr = toreturnstr + "d" + str(i) + "=0"
            if i == todateasint:
                continue
            toreturnstr = toreturnstr + " and "
    return toreturnstr


def getRoomAvailability(  fromdate, todate, hotelid, nbadult, nbchildren, nbrooms):
    sql1 = " SELECT roomManager_roomtype.id,roomManager_roomtype.capacity ,roomManager_roomtype.type_name,roomManager_roomtype.price_per_day FROM roomManager_room " \
           " INNER JOIN roomManager_roomtype on roomManager_room.rtype_id = roomManager_roomtype.id " \
           " INNER JOIN roomManager_availability_room on roomManager_room.id = roomManager_availability_room.room_id "
    sql = str(sql1) + " where " + getwhereofAvalabilitydays(fromdate, todate)
    if hotelid > 0:
        sql = str(sql) + " And room_manager_room.hotelid= " + str(hotelid)

    if nbadult > 0:
        sql = str(sql) + " And room_manager_roomtype.capacity>= " + str(nbadult + nbchildren)

    print(sql)

    with connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchall()
        print(row)



def getview(request):
    sql = getRoomAvailability( '2022-01-01', '2022-01-02', 0, 0, 0, 0)

    return render(request, "availabilityroom.html", {})

from django.contrib.auth.mixins import LoginRequiredMixin
from wkhtmltopdf.views import PDFTemplateView
from .models import *
from django.conf import settings
from datetime import datetime, date
from django.db import connection
import random
from django.http import HttpResponse, FileResponse
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
from datetime import date, datetime
from booking.models import RoomBooked, Reservation
from roomManager.models import RoomType
import datetime
from django.db.models.functions import Now
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def test_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    books = Reservation.objects.all()

    lines = []
    for book in books:
        res = {'type': book.type,
               'booking_status': book.booking_status,
               'customer': book.customer.First_Name,
               'From_date': book.From_date,
               'To_date': book.To_date,
               }
        lines.append(res)

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='t1.pdf')


class TodayCheckin(LoginRequiredMixin, PDFView):
    template_name = 'reportbooking\CheckIn.html'

    def get_context_data(self, *args,  **kwargs):

        chechdate = date.today()
        print(chechdate)
        sql1 = "SELECT booking_RoomBooked.nb_Adults, booking_RoomBooked.nb_Children, DATE(booking_Reservation.to_date)," \
               "booking_Reservation.type, roomManager_RoomType.type_name" \
               "FROM booking_RoomBooked " \
               "INNER JOIN booking_reservation on booking_RoomBooked.booking_id = booking_reservation.id " \
               "INNER JOIN roomManager_roomtype on booking_RoomBooked.type_id = roomManager_roomtype.id " \
               "WHERE DATE(booking_Reservation.From_date) = '" + chechdate.strftime("%Y-%m-%d") + "'"

        print(sql1)
        context = super().get_context_data(*args, **kwargs)
        checkin = []

        with connection.cursor() as cursor:
            cursor.execute(sql1)
            rows = cursor.fetchall()

        for row in rows:
            check = {
                'type': row[4],
                'reservation': row[3],
                'checkout': row[2],
                'adults': row[0],
                'children': row[1],

            }
            checkin.append(check)

        context['check'] = checkin
        return context


class TodayCheckout(LoginRequiredMixin, PDFView):
    template_name = 'reportbooking\CheckOut.html'

    def get_context_data(self, *args,  **kwargs):

        chechdate = date.today()
        print(chechdate)

        sql1 = "SELECT booking_RoomBooked.nb_Adults, booking_RoomBooked.nb_Children," \
               "DATE(booking_Reservation.From_date)," \
               "booking_Reservation.type, roomManager_RoomType.type_name, " \
               "FROM booking_RoomBooked " \
               "INNER JOIN booking_reservation on booking_RoomBooked.booking_id = booking_reservation.id " \
               "INNER JOIN roomManager_roomtype on booking_RoomBooked.type_id = roomManager_roomtype.id " \
               "WHERE DATE(booking_Reservation.To_date) = '" + chechdate.strftime("%Y-%m-%d") + "'"

        print(sql1)
        context = super().get_context_data(*args, **kwargs)
        checkout = []

        with connection.cursor() as cursor:
            cursor.execute(sql1)
            rows = cursor.fetchall()

        for row in rows:
            check = {
                'type': row[4],
                'reservation': row[3],
                'checkin': row[2],
                'adults': row[0],
                'children': row[1],

            }
            checkout.append(check)

        context['check'] = checkout
        return context


class CurrentVisitor(LoginRequiredMixin, PDFView):
    template_name = 'reportbooking\CurrentVisitor.html'

    def get_context_data(self, *args,  **kwargs):

        chechdate = date.today()
        print(chechdate)

        sql1 = "SELECT booking_Visitor.First_name, booking_Visitor.Last_Name," \
               "booking_Visitor.nationality,booking_Visitor.Identity_card_type," \
               "booking_Visitor.Identity_Card_number, DATE(booking_Visitor.birth_date) " \
               "FROM booking_CheckInVisitor " \
               "INNER JOIN booking_visitor on booking_CheckInVisitor.visitor_id = booking_visitor.id" \
               "INNER JOIN booking_CheckIn on booking_CheckInVisitor.checkin_id = booking_CheckIn.id" \
               "WHERE DATE(booking_CheckIn.check_out_date) >= '" + chechdate.strftime("%Y-%m-%d") + "'"

        print(sql1)
        context = super().get_context_data(*args, **kwargs)
        visitor = []

        with connection.cursor() as cursor:
            cursor.execute(sql1)
            rows = cursor.fetchall()

        for row in rows:
            visitor1 = {
                'First_name': row[0],
                'Last_Name': row[1],
                'nationality': row[2],
                'Identity_card_type': row[3],
                'Identity_Card_number': row[4],
                'birth_date': row[5],
            }
            visitor.append(visitor1)

        context['visitor'] = visitor
        return context


class AllVisitor(LoginRequiredMixin, PDFView):
    template_name = 'reportbooking\CurrentVisitor.html'

    def get_context_data(self, *args,  **kwargs):

        chechdate = date.today()
        print(chechdate)

        sql1 = "SELECT booking_Visitor.First_name, booking_Visitor.Last_Name," \
               "booking_Visitor.nationality,booking_Visitor.Identity_card_type," \
               "booking_Visitor.Identity_Card_number, DATE(booking_Visitor.birth_date) " \
               "FROM booking_Visitor "

        print(sql1)
        context = super().get_context_data(*args, **kwargs)
        visitor = []

        with connection.cursor() as cursor:
            cursor.execute(sql1)
            rows = cursor.fetchall()

        for row in rows:
            visitor1 = {
                'First_name': row[0],
                'Last_Name': row[1],
                'nationality': row[2],
                'Identity_card_type': row[3],
                'Identity_Card_number': row[4],
                'birth_date': row[5],
            }
            visitor.append(visitor1)

        context['visitor'] = visitor
        return context


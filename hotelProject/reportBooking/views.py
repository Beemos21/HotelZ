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


# Create your views here.


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

    def get_context_data(self, *args, **kwargs):
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

    def get_context_data(self, *args, **kwargs):
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

    def get_context_data(self, *args, **kwargs):
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

    def get_context_data(self, *args, **kwargs):
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


def getWhereAvalabilitydays(fromdate, todate, availableornot):
    fromdateasdate = datetime.datetime.strptime(fromdate, '%Y-%m-%d')
    fromdateasint = int(fromdateasdate.strftime('%j'))

    todateasdate = datetime.datetime.strptime(todate, '%Y-%m-%d')
    todateasint = int(todateasdate.strftime('%j'))

    toreturnstr = ""
    if todateasint >= fromdateasint:
        for i in range(fromdateasint, todateasint + 1):
            toreturnstr = toreturnstr + "roomManager_availability_room.d" + str(i) + "=" + str(availableornot)
            if i == todateasint:
                continue
            toreturnstr = toreturnstr + " and "
    else:
        intermediate_str = str(fromdateasdate.year) + str("-12-31")
        intermediatedate = datetime.strptime(intermediate_str, '%Y-%m-%d')

        intermediateasint = int(intermediatedate.strftime('%j'))

        for i in range(fromdateasint, intermediateasint + 1):
            toreturnstr = toreturnstr + "roomManager_availability_room.d" + str(i) + "=" + str(availableornot)
            # if i==intermediateasint :
            #     continue
            toreturnstr = toreturnstr + " and "

        # toreturnstr= toreturnstr + " and "

        for i in range(1, todateasint + 1):
            toreturnstr = toreturnstr + "roomManager_availability_room.d" + str(i) + "=" + availableornot
            if i == todateasint:
                continue
            toreturnstr = toreturnstr + " and "
    return toreturnstr


def getRoomAvailability(fromdate, todate, hotelid, availableornot, RoomTypeid):
    sql1 = " SELECT roomManager_roomtype.id,roomManager_roomtype.type_name, roomManager_room.id,roomManager_roomtype.area " \
           " FROM roomManager_room " \
           " INNER JOIN roomManager_roomtype on roomManager_room.rtype_id = roomManager_roomtype.id" \
           " INNER JOIN roomManager_availability_room on roomManager_room.id = roomManager_availability_room.room_id "

    sql = str(sql1) + " where " + getWhereAvalabilitydays(fromdate, todate, availableornot)

    if int(hotelid) > 0:
        sql = str(sql) + " And roomManager_room.hotel_id= " + str(hotelid)

    sql = str(sql) + " And roomManager_RoomType.id= '" + str(RoomTypeid) + "'"

    print(sql)
    roomslist = []

    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            room1 = {
                'roomTypeid': row[0],
                'type_name': row[1],
                'room_id': row[2],
                'area': row[3],
                # 'countofroom': row[2],
            }
            roomslist.append(room1)
    # print(roomslist)
    return roomslist


def getRoomTypes():
    sql = "SELECT roomManager_roomtype.id, roomManager_roomtype.type_name, roomManager_roomtype.price_per_day, " \
          "roomManager_roomtype.area, roomManager_roomtype.bedType, roomManager_roomtype.capacity " \
          "FROM roomManager_roomtype "

    print(sql)
    roomslist = []

    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            type1 = {
                'roomTypeid': row[0],
                'type_name': row[1],
                'area': row[3],
                'price_per_day': row[2],
                'bedType': row[4],
                'capacity': row[5],
            }
            roomslist.append(type1)
    # print(roomslist)
    return roomslist


def searchForRoomAvailabilityViews(request):
    if 'FormRoomAvailability' in request.GET:
        print(request.GET)

        fromDate = request.GET['from_date']
        toDate = request.GET['to_date']
        hotelid = request.GET['Hotel_id']

        roomtypes = getRoomTypes()
        print(roomtypes)

        totalAvailable = 0
        totalReserved = 0
        rtypeList = []
        for z in roomtypes:
            tyid = z['roomTypeid']
            roomTname = z['type_name']
            roomTarea = z['area']
            roomTprice = z['price_per_day']
            bedType = z['bedType']
            capacity = z['capacity']

            availableRooms = getRoomAvailability(fromDate, toDate, hotelid, 0, tyid)
            reservedRooms = getRoomAvailability(fromDate, toDate, hotelid, 1, tyid)

            countAvailable = 0
            countReserved = 0

            for x in availableRooms:
                countAvailable += 1

            for y in reservedRooms:
                countReserved += 1

            forcount = {'countAvailable': countAvailable,
                        'countReserved': countReserved,
                        'roomTname': roomTname,
                        'roomTarea': roomTarea,
                        'roomTprice': roomTprice,
                        'bedType': bedType,
                        'capacity': capacity,
                        }
            rtypeList.append(forcount)
            # return rtypeList

            totalAvailable += countAvailable  # all available roms from any type
            totalReserved += countReserved

        countData = {
            # 'countAvailable': countAvailable,
            #  'countReserved': countReserved,

            'rtypeList': rtypeList,
            'totalAvailable': totalAvailable,
            'totalReserved': totalReserved,

            'roomtypes': roomtypes,
            'fromDate': fromDate,
            'toDate': toDate,
        }

        return render(request, 'roomAvailabilityReport.html', countData)
    else:
        return render(request, "roomAvailabilityForm.html")

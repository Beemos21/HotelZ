from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from datetime import datetime
from datetime import date
from django.db import connection
# from .serializers import AvalabilitySerializer, BranchesSerializer, RoomTypeSerializer
from rest_framework import mixins, viewsets
from django_renderpdf.views import PDFView
# from .forms import FormRoomAvailability


# Create your views here.


def getWhereAvalabilitydays(fromdate, todate, availableornot):
    fromdateasdate = datetime.strptime(fromdate, '%Y-%m-%d')
    fromdateasint = int(fromdateasdate.strftime('%j'))

    todateasdate = datetime.strptime(todate, '%Y-%m-%d')
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


def getRoomAvailability(fromdate, todate, hotelid, availableornot, RoomTypeName):
    sql1 = " SELECT roomManager_roomtype.id,roomManager_roomtype.type_name, roomManager_room.id " \
           " FROM roomManager_room " \
           " INNER JOIN roomManager_roomtype on roomManager_room.rtype_id = roomManager_roomtype.id" \
           " INNER JOIN roomManager_availability_room on roomManager_room.id = roomManager_availability_room.room_id "

    sql = str(sql1) + " where " + getWhereAvalabilitydays(fromdate, todate, availableornot)

    if int(hotelid) > 0:
        sql = str(sql) + " And roomManager_room.hotel_id= " + str(hotelid)

    sql = str(sql) + " And roomManager_RoomType.type_name= '" + RoomTypeName + "'"

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
                # 'countofroom': row[2],
            }
            roomslist.append(room1)
    # print(roomslist)
    return roomslist


# def home_view(request):
#     context = {}
#     context['form'] = FormRoomAvailability()
#     return render(request, "home.html", context)


def searchForRoomAvailabilityViews(request):
    if 'FormRoomAvailability' in request.GET:
        # print('FormRoomAvailability')
        print(request.POST)

        fromDate = request.GET['from_date']
        toDate = request.GET['to_date']

        # roomAvailabilityReportViews(fromDate, toDate)
        availableRoomsSR = getRoomAvailability(fromDate, toDate, 1, 0, 'Single room')
        reservedRoomsSR = getRoomAvailability(fromDate, toDate, 1, 1, 'Single room')
        countASR = 0
        countRSR = 0
        for x in availableRoomsSR:
            countASR += 1
        for y in reservedRoomsSR:
            countRSR += 1

        availableRoomsTR = getRoomAvailability(fromDate, toDate, 1, 0, 'Twin room')
        reservedRoomsTR = getRoomAvailability(fromDate, toDate, 1, 1, 'Twin room')
        countATR = 0
        countRTR = 0
        for x in availableRoomsTR:
            countATR += 1
        for y in reservedRoomsTR:
            countRTR += 1

        availableRoomsDR = getRoomAvailability(fromDate, toDate, 1, 0, 'Double room')
        reservedRoomsDR = getRoomAvailability(fromDate, toDate, 1, 1, 'Double room')
        countADR = 0
        countRDR = 0
        for x in availableRoomsDR:
            countADR += 1
        for y in reservedRoomsDR:
            countRDR += 1

        availableRoomsTrR = getRoomAvailability(fromDate, toDate, 1, 0, 'Triple room')
        reservedRoomsTrR = getRoomAvailability(fromDate, toDate, 1, 1, 'Triple room')
        countATrR = 0
        countRTrR = 0
        for x in availableRoomsTrR:
            countATrR += 1
        for y in reservedRoomsTrR:
            countRTrR += 1

        availableRoomsQR = getRoomAvailability(fromDate, toDate, 1, 0, 'Quad room')
        reservedRoomsQR = getRoomAvailability(fromDate, toDate, 1, 1, 'Quad room')
        countAQR = 0
        countRQR = 0
        for x in availableRoomsQR:
            countAQR += 1
        for y in reservedRoomsQR:
            countRQR += 1

        availableRoomsDDR = getRoomAvailability(fromDate, toDate, 1, 0, 'Double-Double room')
        reservedRoomsDDR = getRoomAvailability(fromDate, toDate, 1, 1, 'Double-Double room')
        countADDR = 0
        countRDDR = 0
        for x in availableRoomsDDR:
            countADDR += 1
        for y in reservedRoomsDDR:
            countRDDR += 1

        availableRoomsQuR = getRoomAvailability(fromDate, toDate, 1, 0, 'Queen room')
        reservedRoomsQuR = getRoomAvailability(fromDate, toDate, 1, 1, 'Queen room')
        countAQuR = 0
        countRQuR = 0
        for x in availableRoomsQuR:
            countAQuR += 1
        for y in reservedRoomsQuR:
            countRQuR += 1

        availableRoomsS = getRoomAvailability(fromDate, toDate, 1, 0, 'Suite')
        reservedRoomsS = getRoomAvailability(fromDate, toDate, 1, 1, 'Suite')
        countAS = 0
        countRS = 0
        for x in availableRoomsS:
            countAS += 1
        for y in reservedRoomsS:
            countRS += 1

        availableRoomsPS = getRoomAvailability(fromDate, toDate, 1, 0, 'Suite')
        reservedRoomsPS = getRoomAvailability(fromDate, toDate, 1, 1, 'Suite')
        countAPS = 0
        countRPS = 0
        for x in availableRoomsPS:
            countAPS += 1
        for y in reservedRoomsPS:
            countRPS += 1

        availableRoomsSt = getRoomAvailability(fromDate, toDate, 1, 0, 'Studio')
        reservedRoomsSt = getRoomAvailability(fromDate, toDate, 1, 1, 'Studio')
        countASt = 0
        countRSt = 0
        for x in availableRoomsSt:
            countASt += 1
        for y in reservedRoomsSt:
            countRSt += 1

        availableRoomsCR = getRoomAvailability(fromDate, toDate, 1, 0, 'Connecting rooms')
        reservedRoomsCR = getRoomAvailability(fromDate, toDate, 1, 1, 'Connecting rooms')
        countACR = 0
        countRCR = 0
        for x in availableRoomsCR:
            countACR += 1
        for y in reservedRoomsCR:
            countRCR += 1

        availableRoomsJS = getRoomAvailability(fromDate, toDate, 1, 0, 'Junior Suite')
        reservedRoomsJS = getRoomAvailability(fromDate, toDate, 1, 1, 'Junior Suite')
        countAJS = 0
        countRJS = 0
        for x in availableRoomsJS:
            countAJS += 1
        for y in reservedRoomsJS:
            countRJS += 1

        totalAvailable = countASR + countATR + countADR + countATrR + countAQR + countADDR + countAQuR + countAS \
                         + countAPS + countASt + countACR + countAJS  # all available roms from any type
        totalReserved = countRSR + countRTR + countRDR + countRTrR + countRQR + countRDDR + countRQuR + countRS \
                        + countRPS + countRSt + countRCR + countRJS

        countData = {'countAvailableSR': countASR,
                     'countReservedSR': countRSR,
                     'countAvailableTR': countATR,
                     'countReservedTR': countRTR,
                     'countAvailableDR': countADR,
                     'countReservedDR': countRDR,
                     'countAvailableTrR': countATrR,
                     'countReservedTrR': countRTrR,
                     'countAvailableQR': countAQR,
                     'countReservedQR': countRQR,
                     'countAvailableDDR': countADDR,
                     'countReservedDDR': countRDDR,
                     'countAvailableQuR': countAQuR,
                     'countReservedQuR': countRQuR,
                     'countAvailableS': countAS,
                     'countReservedS': countRS,
                     'countAvailablePS': countAPS,
                     'countReservedPS': countRPS,
                     'countAvailableSt': countASt,
                     'countReservedSt': countRSt,
                     'countAvailableCR': countACR,
                     'countReservedCR': countRCR,
                     'countAvailableJS': countAJS,
                     'countReservedJS': countRJS,

                     'totalAvailable': totalAvailable,
                     'totalReserved': totalReserved,
                     'fromDate': fromDate,
                     'toDate': toDate,

                     }

        return render(request, 'roomAvailabilityReport.html', countData)
    else:
        return render(request, "roomAvailabilityForm.html")


# def searchForRoomAvailabilityPDFViews(request):
#     if 'FormRoomAvailability' in request.GET:
#         fromDate = request.GET['from_date']
#         toDate = request.GET['to_date']
#
#         # roomAvailabilityReportViews(fromDate, toDate)
#         availableRoomsSR = getRoomAvailability(fromDate, toDate, 1, 0, 'Single room')
#         reservedRoomsSR = getRoomAvailability(fromDate, toDate, 1, 1, 'Single room')
#         countASR = 0
#         countRSR = 0
#         for x in availableRoomsSR:
#             countASR += 1
#         for y in reservedRoomsSR:
#             countRSR += 1
#
#         availableRoomsTR = getRoomAvailability(fromDate, toDate, 1, 0, 'Twin room')
#         reservedRoomsTR = getRoomAvailability(fromDate, toDate, 1, 1, 'Twin room')
#         countATR = 0
#         countRTR = 0
#         for x in availableRoomsTR:
#             countATR += 1
#         for y in reservedRoomsTR:
#             countRTR += 1
#
#         availableRoomsDR = getRoomAvailability(fromDate, toDate, 1, 0, 'Double room')
#         reservedRoomsDR = getRoomAvailability(fromDate, toDate, 1, 1, 'Double room')
#         countADR = 0
#         countRDR = 0
#         for x in availableRoomsDR:
#             countADR += 1
#         for y in reservedRoomsDR:
#             countRDR += 1
#
#         availableRoomsTrR = getRoomAvailability(fromDate, toDate, 1, 0, 'Triple room')
#         reservedRoomsTrR = getRoomAvailability(fromDate, toDate, 1, 1, 'Triple room')
#         countATrR = 0
#         countRTrR = 0
#         for x in availableRoomsTrR:
#             countATrR += 1
#         for y in reservedRoomsTrR:
#             countRTrR += 1
#
#         availableRoomsQR = getRoomAvailability(fromDate, toDate, 1, 0, 'Quad room')
#         reservedRoomsQR = getRoomAvailability(fromDate, toDate, 1, 1, 'Quad room')
#         countAQR = 0
#         countRQR = 0
#         for x in availableRoomsQR:
#             countAQR += 1
#         for y in reservedRoomsQR:
#             countRQR += 1
#
#         availableRoomsDDR = getRoomAvailability(fromDate, toDate, 1, 0, 'Double-Double room')
#         reservedRoomsDDR = getRoomAvailability(fromDate, toDate, 1, 1, 'Double-Double room')
#         countADDR = 0
#         countRDDR = 0
#         for x in availableRoomsDDR:
#             countADDR += 1
#         for y in reservedRoomsDDR:
#             countRDDR += 1
#
#         availableRoomsQuR = getRoomAvailability(fromDate, toDate, 1, 0, 'Queen room')
#         reservedRoomsQuR = getRoomAvailability(fromDate, toDate, 1, 1, 'Queen room')
#         countAQuR = 0
#         countRQuR = 0
#         for x in availableRoomsQuR:
#             countAQuR += 1
#         for y in reservedRoomsQuR:
#             countRQuR += 1
#
#         availableRoomsS = getRoomAvailability(fromDate, toDate, 1, 0, 'Suite')
#         reservedRoomsS = getRoomAvailability(fromDate, toDate, 1, 1, 'Suite')
#         countAS = 0
#         countRS = 0
#         for x in availableRoomsS:
#             countAS += 1
#         for y in reservedRoomsS:
#             countRS += 1
#
#         availableRoomsPS = getRoomAvailability(fromDate, toDate, 1, 0, 'Suite')
#         reservedRoomsPS = getRoomAvailability(fromDate, toDate, 1, 1, 'Suite')
#         countAPS = 0
#         countRPS = 0
#         for x in availableRoomsPS:
#             countAPS += 1
#         for y in reservedRoomsPS:
#             countRPS += 1
#
#         availableRoomsSt = getRoomAvailability(fromDate, toDate, 1, 0, 'Studio')
#         reservedRoomsSt = getRoomAvailability(fromDate, toDate, 1, 1, 'Studio')
#         countASt = 0
#         countRSt = 0
#         for x in availableRoomsSt:
#             countASt += 1
#         for y in reservedRoomsSt:
#             countRSt += 1
#
#         availableRoomsCR = getRoomAvailability(fromDate, toDate, 1, 0, 'Connecting rooms')
#         reservedRoomsCR = getRoomAvailability(fromDate, toDate, 1, 1, 'Connecting rooms')
#         countACR = 0
#         countRCR = 0
#         for x in availableRoomsCR:
#             countACR += 1
#         for y in reservedRoomsCR:
#             countRCR += 1
#
#         availableRoomsJS = getRoomAvailability(fromDate, toDate, 1, 0, 'Junior Suite')
#         reservedRoomsJS = getRoomAvailability(fromDate, toDate, 1, 1, 'Junior Suite')
#         countAJS = 0
#         countRJS = 0
#         for x in availableRoomsJS:
#             countAJS += 1
#         for y in reservedRoomsJS:
#             countRJS += 1
#
#         totalAvailable = countASR + countATR + countADR + countATrR + countAQR + countADDR + countAQuR + countAS \
#                          + countAPS + countASt + countACR + countAJS  # all available roms from any type
#         totalReserved = countRSR + countRTR + countRDR + countRTrR + countRQR + countRDDR + countRQuR + countRS \
#                         + countRPS + countRSt + countRCR + countRJS
#
#         countData = {'countAvailableSR': countASR,
#                      'countReservedSR': countRSR,
#                      'countAvailableTR': countATR,
#                      'countReservedTR': countRTR,
#                      'countAvailableDR': countADR,
#                      'countReservedDR': countRDR,
#                      'countAvailableTrR': countATrR,
#                      'countReservedTrR': countRTrR,
#                      'countAvailableQR': countAQR,
#                      'countReservedQR': countRQR,
#                      'countAvailableDDR': countADDR,
#                      'countReservedDDR': countRDDR,
#                      'countAvailableQuR': countAQuR,
#                      'countReservedQuR': countRQuR,
#                      'countAvailableS': countAS,
#                      'countReservedS': countRS,
#                      'countAvailablePS': countAPS,
#                      'countReservedPS': countRPS,
#                      'countAvailableSt': countASt,
#                      'countReservedSt': countRSt,
#                      'countAvailableCR': countACR,
#                      'countReservedCR': countRCR,
#                      'countAvailableJS': countAJS,
#                      'countReservedJS': countRJS,
#
#                      'totalAvailable': totalAvailable,
#                      'totalReserved': totalReserved,
#                      'fromDate': fromDate,
#                      'toDate': toDate,
#
#                      }
#
#         class RoomAvailabilityReportPDFView(LoginRequiredMixin, PDFView):
#             template_name = 'roomAvailabilityReport.html'
#
#             def get_context_data(self, *args, **kwargs):
#                 context = super().get_context_data(*args, **kwargs)
#                 context = countData
#                 return context
#
#             # return render(request, "roomAvailabilityReport.html", context)
#         # return render(request, 'roomAvailabilityReport.html', countData)
#     else:
#         return render(request, "roomAvailabilityForm.html")

from django.views import generic
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from .models import User, Room, Reservation
from .serializers import ReservationSerializer, RoomSerializer
from rest_framework import status, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime


class MakeReservation(generics.CreateAPIView):
    serializer_class = ReservationSerializer


class OverviewReport(generic.ListView):
    queryset = Reservation.objects.all()
    template_name = 'report.html'
    context_object_name = 'report'


def convert_date(date: str) -> datetime.date:
    date_str = date

    date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
    return date_object


def has_overlap(
        start_date: datetime,
        end_date: datetime,
        event_start_date: datetime,
        event_end_date: datetime
):
    if event_start_date <= end_date <= event_end_date:
        return True

    if event_start_date <= start_date <= event_end_date:
        return True

    if event_start_date >= start_date and event_end_date <= end_date:
        return True

    if event_start_date <= start_date and event_end_date >= end_date:
        return True
    return False


@api_view(["GET"])
def get_empty_rooms_in_date_range(request):
    user_from_date = request.query_params.get("from", None)
    user_until_date = request.query_params.get("to", None)

    if not (user_until_date and user_until_date):
        return Response({
            "error": "the range is invalid"
        }, status=status.HTTP_404_NOT_FOUND)

    fromdate = convert_date(user_from_date)
    todate = convert_date(user_until_date)

    all_reservation_periods = Reservation.objects.all().values("room__id", "FromDate", "toDate")
    all_available_rooms = []

    for period in all_reservation_periods:
        if not has_overlap(period['FromDate'], period['toDate'], fromdate, todate):
            all_available_rooms.append(period['room__id'])

        elif has_overlap(period['FromDate'], period['toDate'], fromdate, todate):
            all_available_rooms.append(period['room__id'])
        else:
            index = all_available_rooms.index(period['room__id'])
            del all_available_rooms[index]

    ser = RoomSerializer(Room.objects.exclude(id__in=all_available_rooms), many=True)
    return Response(ser.data, status=status.HTTP_200_OK)


class ReservationForPerson(APIView):

    def post(self, request):

        serializer = ReservationSerializer(data=request.data)

        if serializer.is_valid():

            from_date = convert_date(request.data.get('FromDate'))

            to_date = convert_date(request.data.get('toDate'))

            if from_date >= to_date:
                return Response({

                    "error": "Invalid date range"

                }, status=status.HTTP_400_BAD_REQUEST)

            reservation_data = {

                'FromDate': from_date,

                'toDate': to_date,

                'customer': None,

                'room': None,

                'Phone': '',

                'Email': '',
            }
            
            all_reservation_periods = Reservation.objects.all().values("room__id", "FromDate", "toDate")
            all_available_rooms = []

        for period in all_reservation_periods:
            if not has_overlap(period['FromDate'], period['toDate'], fromdate, todate):
                all_available_rooms.append(period['room__id'])

            elif has_overlap(period['FromDate'], period['toDate'], fromdate, todate):
                all_available_rooms.append(period['room__id'])
            else:
                index = all_available_rooms.index(period['room__id'])
                del all_available_rooms[index]

            serializer = ReservationSerializer(data=reservation_data)

            if serializer.is_valid():

                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)

            else:

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

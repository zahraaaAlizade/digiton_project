from django.template.defaulttags import url
from django.urls import path, include
from .views import MakeReservation, OverviewReport, get_empty_rooms_in_date_range, ReservationForPerson
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('report/', OverviewReport.as_view()),
    path('reserve/', MakeReservation.as_view()),
    path('r-person/', ReservationForPerson.as_view()),
    path('empty-rooms/', get_empty_rooms_in_date_range)
]

from django.contrib import admin
from .models import User, Room, Reservation


@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'role']


@admin.register(Room)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'currentStatus']


@admin.register(Reservation)
class PostAdmin(admin.ModelAdmin):
    list_display = ['customer', 'room', 'Phone', 'Email', 'created_time']


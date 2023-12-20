from django.db import models


class User(models.Model):
    class RoleChoices(models.TextChoices):
        CUSTOMER = "C", "CUSTOMER"
        ADMIN = "L", "LISTING OWNER"

    username = models.CharField(max_length=50)
    role = models.CharField(max_length=2, choices=RoleChoices.choices)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Room(models.Model):
    class RoomStatusChoices(models.TextChoices):
        IDLE = "I", "IDLE"
        FULL = "F", "FULL"

    number = models.CharField(max_length=5)
    currentStatus = models.CharField(max_length=2, choices=RoomStatusChoices.choices)

    def __str__(self):
        return '{}- {}'.format(self.pk, self.number)


class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    Phone = models.CharField(max_length=11, blank=True)
    Email = models.EmailField(max_length=40, blank=True)
    FromDate = models.DateField()
    toDate = models.DateField()
    created_time = models.DateTimeField(auto_now_add=True)

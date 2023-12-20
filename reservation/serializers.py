from rest_framework import serializers
from .models import User, Room, Reservation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'role']


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['customer', 'room', 'Phone', 'Email', 'FromDate', 'toDate']

#
# class RezervationPersonSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     FromDate = serializers.DateField()
#     toDate = serializers.DateField()

class RezervationPersonSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=100)

    customer_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True)

    room_id = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all(), allow_null=True)

    Phone = serializers.CharField(max_length=11)

    Email = serializers.EmailField(max_length=40)

    FromDate = serializers.DateField()

    toDate = serializers.DateField()


from django.contrib.auth.models import User
from rest_framework import serializers


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
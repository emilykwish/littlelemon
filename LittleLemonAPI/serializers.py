from django.contrib.auth.models import User
from rest_framework import serializers, generics
from .models import MenuItem  # Ensure you import your MenuItem model

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem  # Specifies the model to serialize
        fields = '__all__'  # Indicates that all fields in the model should be included in the serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'  / ['url', 'username', 'email', 'groups']
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
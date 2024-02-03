from django.shortcuts import render
from .models import MenuItem
from .serializers import MenuItemSerializer, UserSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from restaurant.views import BookingViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics, viewsets
from django.contrib.auth.models import User


@api_view()

@permission_classes([IsAuthenticated])

def msg(request):
    return Response({"message":"This view is protected"})

# Create your views here.

class MenuItemsView(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = MenuItem.objects.all()
  serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]  # Optional: Restrict this view to admin users only

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

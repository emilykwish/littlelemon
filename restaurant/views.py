from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from .serializers import BookingSerializer
from .serializers import MenuItemSerializer

# Create your views here.

def sayHello(request):
    return HttpResponse('Hello World')

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# class BookingView(APIView):
class BookingViewSet(viewsets.ModelViewSet):
    def get(self,request):
        items = booking.objects.all()
        serializer = BookingSerializer(items, many= True)
        permission_classes = [IsAuthenticated]
        return Response(serializer.data) #Return JSON
        
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # def post(self, request):
    #     serializer = MenuSerializer(data=request.data)

    #     if serializer.is.valid():
    #         serializer.save()
    #         return Response({"status": "success", "data": serializer.data})


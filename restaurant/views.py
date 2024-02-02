from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view

from .models import Booking, Menu
from .serializers import BookingSerializer
from .serializers import MenuSerializer

# Create your views here.

def sayHello(request):
    return HttpResponse('Hello World')

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class BookingView(APIView):
    def get(self,request):
        items = booking.objects.all()
        serializer = BookingSerializer(items, many= True)
        return Response(serializer.data) #Return JSON

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # def post(self, request):
    #     serializer = MenuSerializer(data=request.data)

    #     if serializer.is.valid():
    #         serializer.save()
    #         return Response({"status": "success", "data": serializer.data})


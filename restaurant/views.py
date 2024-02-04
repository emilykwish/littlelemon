from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User

from .models import MenuItem, Booking
from .serializers import BookingSerializer, UserSerializer, MenuItemSerializer

# Create your views here.

@api_view()

@permission_classes([IsAuthenticated])

def msg(request):
    return Response({"message":"This view is protected"})


def sayHello(request):
    return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})
        
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]   
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# class BookingView(APIView):
# class BookingViewSet(viewsets.ModelViewSet):
#     def get(self,request):
#         items = booking.objects.all()
#         serializer = BookingSerializer(items, many= True)
#         permission_classes = [IsAuthenticated]
#         return Response(serializer.data) #Return JSON



#     def post(self, request):
#         serializer = MenuSerializer(data=request.data)

#         if serializer.is.valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})


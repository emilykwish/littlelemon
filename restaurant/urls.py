from django.contrib import admin 
from django.urls import path 
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import sayHello, MenuItemsView, BookingViewSet

urlpatterns = [ 
    path('', sayHello, name='sayHello'), 
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),  
    path('api-token-auth/', obtain_auth_token),
    # path('menu/', MenuView.as_view()),
    # path('booking/', bookingview.as_view()),
]
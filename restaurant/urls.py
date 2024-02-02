from django.contrib import admin 
from django.urls import path 
from . import views
from .views import sayHello, MenuItemsView, BookingView
  
urlpatterns = [ 
    path('', sayHello, name='sayHello'), 
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),  
    # path('menu/', MenuView.as_view()),
    # path('booking/', bookingview.as_view()),
]
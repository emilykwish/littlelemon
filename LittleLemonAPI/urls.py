from django.urls import path
from rest_framework import routers
from . import views
from .views import UserCreate
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('register/', views.UserCreate.as_view(), name='user-register'),
]
from django.test import TestCase
# from LittleLemonAPI.models import MenuItem
from django.urls import reverse
from restaurant.models import MenuItem, Booking
from rest_framework.test import APIClient
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Setup code to create Menu instances
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)

    def test_getall(self):
        # Test to retrieve all Menu objects
        client = APIClient()
        response = client.get(reverse('menu-items'))  # Assuming the URL name for your Menu list view is 'menu-list'
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
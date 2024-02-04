from django.test import TestCase
# from LittleLemonAPI.models import MenuItem
from django.urls import reverse
from restaurant.models import MenuItem, Booking
from rest_framework.test import APIClient
from restaurant.serializers import MenuItemSerializer

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = item.get_item()
        self.assertEqual(item, "IceCream : 80")
        

        

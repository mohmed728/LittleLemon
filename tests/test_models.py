from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    
    def test_string (self):
        menu = Menu.objects.create(
            Title = "Ice Cream",
            Price = 20.00,
            inventory = 100
        )
        self.assertEqual(str(menu),"Ice Cream : 20.0")

from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu
from rest_framework.test import APIClient
from restaurant.serializers import MenuSerializer
class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        Menu.objects.create(
            Title="Ice Cream",
            Price=20.00,
            inventory=100
        )

        Menu.objects.create(
            Title="Pizza",
            Price=50.00,
            inventory=200
        )
    def test_getall(self):
        response = self.client.get('/restaurant/menu/')

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
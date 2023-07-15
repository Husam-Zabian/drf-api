from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Car


# Create your tests here.

class CarTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_car = Car.objects.create(brand='Mercedes', owner=testuser1, car_desc="test desc ...")
        test_car.save()

    def cars_model(self):
        car = Car.objects.get(id=1)
        actual_owner= str(car.owner)
        actual_name = str(car.car_brand)
        actual_desc = str(car.car_desc)
        self.assertEqual(actual_owner,"testuser1")
        self.assertEqual(actual_name,"Mercedes")
        self.assertEqual(actual_desc,"test desc ...")

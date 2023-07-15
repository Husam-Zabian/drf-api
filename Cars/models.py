from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Car(models.Model):
    car_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    car_brand = models.CharField(max_length=64)
    car_desc = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

  
    def __str__(self):
        return self.car_brand
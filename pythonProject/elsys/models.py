from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Car(models.Model):
    color = models.CharField(max_length=100)
    made = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=50)
    description = models.TextField()
    year_production = models.IntegerField(default=2000, validators=[MinValueValidator(1), MaxValueValidator(2022)])
    hp = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])

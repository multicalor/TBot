from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Car(models.Model):
    vin = models.CharField(verbose_name='Vin', db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name='Color', max_length=64)
    brend = models.CharField(verbose_name='Brend', max_length=64)
    СAR_TYPES = (
        (1, 'Седан'),
        (2, 'Хэчбек'),
        (3, 'Универсал'),
        (4, 'Купе'),
    )

    car_type = models.IntegerField(verbose_name='Car_Type', choices=СAR_TYPES)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
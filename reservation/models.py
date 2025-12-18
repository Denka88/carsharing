from enum import Enum

from django.conf import settings
from django.db import models

from cars.models import Car
from users.models import CustomUser

class Reservation(models.Model):

    class Meta:
        verbose_name = 'Бронировнаие авто'
        verbose_name_plural = 'Бронирования авто'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()

    PAYMENT_METHODS = [
        ('Card', 'Карта'),
        ('SBP', 'СБП')
    ]

    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('confirmed', 'Подтверждена'),
        ('cancelled', 'Отклонена')
    ]

    payment_method = models.CharField(choices=PAYMENT_METHODS, max_length=20, default='new')
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.car.name} ({self.status}) '
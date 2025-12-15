from enum import Enum

from django.db import models

from cars.models import Car
from users.models import CustomUser

# Create your models here.
class Status(Enum):
    NEW = 'New'
    REJECTED = 'Rejected'
    INACTIVE = 'Inactive'
    APPROVED = 'Approved'

class PaymentMethod(Enum):
    CARD = 'Card'
    SBP = 'SBP'

class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
    payment_method = models.CharField(choices=[(tag.name, tag.value) for tag in PaymentMethod], default=PaymentMethod.CARD.value)
    status = models.CharField(choices=[(tag.name, tag.value) for tag in Status], default=Status.NEW.value)

    def __str__(self):
        return f'{self.user.username}: {self.car.name}. {self.payment_method}. {self.date_start} - {self.date_end}. {self.status}'
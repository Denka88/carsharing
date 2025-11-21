from django.contrib import admin

from cars.models import Car
from cars.models import CarsCharacteristics

# Register your models here.
admin.site.register(Car)
admin.site.register(CarsCharacteristics)
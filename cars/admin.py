from django.contrib import admin

from cars.models import Car, CarsCategories
from cars.models import CarsCharacteristics

# Register your models here.
admin.site.register(Car)
admin.site.register(CarsCharacteristics)
admin.site.register(CarsCategories)
from django.contrib import admin

from cars.models import Car, CarCategory
from cars.models import CarsCharacteristics

# Register your models here.

class CarCharacteristicsInline(admin.TabularInline):
    model = CarsCharacteristics
    extra = 1

class CarAdmin(admin.ModelAdmin):
    inlines = [CarCharacteristicsInline]

admin.site.register(Car, CarAdmin)
admin.site.register(CarCategory)
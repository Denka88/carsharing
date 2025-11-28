from django.db import models

# Create your models here.
class CarCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категрия авто'
        verbose_name_plural = 'Категории авто'

    def __str__(self):
        return f'{self.name}'

class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    color = models.CharField(max_length=100)
    year = models.PositiveIntegerField(blank=True, null=True)
    is_available = models.BooleanField(default=True)

    category = models.ForeignKey(
        CarCategory,
        on_delete=models.CASCADE,
        related_name='cars',
        null=True,
    )

    class Meta:
        verbose_name = 'Авто'
        verbose_name_plural = 'Авто'

    def __str__(self):
        return f"{self.name} ({self.year}) - {self.price}"

class CarsCharacteristics(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='characteristics'
    )

    class Meta:
        verbose_name = 'Характеристика авто',
        verbose_name_plural = 'Характеристики авто'

    def __str__(self):
        return f"{self.name}: - {self.description}"
from django.http import HttpResponse
from django.shortcuts import render

from cars.models import Car, CarCategory

# Create your views here.

cars = Car.objects.all()
def index(request):
    return render(request, "index.html")

def cars_page(request):
    categories = CarCategory.objects.all()
    context = {"categories": categories}
    return render(request, "cars.html", context)

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact_us(request):
    return HttpResponse("Страница для связи с нами")
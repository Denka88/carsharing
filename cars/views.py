from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact_us(request):
    return HttpResponse("Страница для связи с нами")
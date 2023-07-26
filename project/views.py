from django.shortcuts import render
from django.http import HttpResponse
from.models import Food

# Create your views here.

def home(request):
    context = {
        'foods': Food.objects.all()
    }
    return render(request, 'project/home.html', context)
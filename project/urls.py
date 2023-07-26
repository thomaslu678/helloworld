from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='Home'),
    path('data/', views.data, name='Data'),

]

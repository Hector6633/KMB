from django.urls import path
from . views import *

urlpatterns = [
    path('index', pooja_booking, name='pooja_booking'),
]
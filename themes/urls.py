from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='index'),
    path('index', feedback_us, name='feedback_us'),
]

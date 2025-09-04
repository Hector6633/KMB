from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='index'),
    path('index', contact_us, name='contact_us'),
]

from django.shortcuts import render, redirect
from . models import *
from service.models import Pooja_Info, Pooja_Info_Table
from django.contrib import messages
# Create your views here.
def index(request):
    data = {
        'blogs': KMB_Blog.objects.all(),
        'pooja_info': Pooja_Info.objects.all(),
        'pooja_table': Pooja_Info_Table.objects.all(),
    }
    return render(request, 'index.html', data)

def contact_us(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            contact_data = Contact_Us.objects.create(name=name, email=email, message=message)
            contact_data.save()
            success_msg = "Successfully Registered"
            messages.success(request, success_msg)
            return redirect('index')
        except Exception as e:
            error_msg = 'Server error try again after few minutes'
            messages.error(request, error_msg)
            return redirect('index')
    return render(request, 'index.html')

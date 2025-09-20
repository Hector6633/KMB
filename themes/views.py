from django.shortcuts import render, redirect
from . models import *
from service.models import Pooja_Name, Nakshatharam
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    data = {
        'blogs': KMB_Blog.objects.all(),
        'pooja_info': Pooja_Name.objects.all(),
        'stars': Nakshatharam.objects.all(),
    }
    return render(request, 'index.html', data)

def feedback_us(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            contact_data = Contact_Us.objects.create(name=name, email=email, message=message)
            contact_data.save()
            subject = "Sree Koodathil Madaswamy Temple"
            message = f"Dear {name},\nThank You for your feedback with KMB Temple.Whether you’re looking for blessings, peace of mind, or a spiritual experience, Lord Madaswamy Temple welcomes everyone with open arms.\nPlease keep this email for your records and do not forward or share any other person.\nFor more details please visit our website at https://127.0.0.1:8000/."
            recipient = email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient],
                fail_silently=False,
            )
            success_msg = "Successfully Registered"
            messages.success(request, success_msg)
            return redirect('index')
        except Exception as e:
            error_msg = 'Server error try again after few minutes'
            messages.error(request, error_msg)
            return redirect('index')
    return render(request, 'index.html')

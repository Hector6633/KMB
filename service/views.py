from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def pooja_booking(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone_number = request.POST.get('number')
            date = request.POST.get('date')
            pooja_name = request.POST.get('pooja_name')
            nakshatharam = request.POST.get('nakshatharam')
            quantity = request.POST.get('quantity')
            booking_data = PoojaBooking.objects.create(name=name, email=email, phone_number=phone_number, booking_date=date, poojaname=pooja_name, nak=nakshatharam, quantity=quantity)
            booking_data.save()
            subject = "Sree Koodathil Madaswamy Temple"
            message = f"Dear {name},\nYou are successfully booked our pooja slot with KMB Temple.Our temple advisor will verify your details and get in touch with you.\nHere are your pooja details:\nEmail:{email}\nPhone Number: {phone_number}\nPooja-Name: {pooja_name}\nNakshatharam: {nakshatharam}\nQuantity: {quantity}\nDate: {date}\nPlease keep this email for your records and do not forward or share any other person.For more details please visit our website at https://127.0.0.1:8000/."
            recipient = email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient],
                fail_silently=False,
            )
            success_msg = 'Successfully Booked'
            messages.success(request, success_msg)
            return redirect('index')
        except Exception as e:
            error_msg = 'Server error try again after few minutes'
            messages.error(request, error_msg)
            return redirect('index')
    return render(request, 'index.html')
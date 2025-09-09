from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages

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
            booking_data = Pooja_Booking.objects.create(name=name, email=email, phone_number=phone_number, date=date, pooja_name=pooja_name, nakshatharam=nakshatharam, quantity=quantity)
            booking_data.save()
            success_msg = 'Successfully Booked'
            messages.success(request, success_msg)
            return redirect('index')
        except Exception as e:
            error_msg = 'Something went wrong'
            messages.error(request, error_msg)
            return redirect('index')
    return render(request, 'index.html')
from django.shortcuts import render, redirect, HttpResponsePermanentRedirect
from django.urls import reverse
from Login_App.models import ProfileModel

# Messages
from django.contrib import messages

# models and forms
from Order_App.models import OrderModel
from Payment_App.models import BillingAddressModel
from Payment_App.forms import BillingAddressForm

# Decorator
from django.contrib.auth.decorators import login_required

# Payment
import requests
import socket
from decimal import Decimal
from sslcommerz import SSLCOMMERZ

# Create your views here.

@login_required
def checkout_view(request):
    title = 'Checkout'
    saved_address = BillingAddressModel.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    print(saved_address)
    form = BillingAddressForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingAddressForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingAddressForm(instance=saved_address)
            messages.success(request, f"Shipping address saved")
    order_qs = OrderModel.objects.filter(user=request.user, ordered=False)
    print(order_qs)
    order_items = order_qs[0].orderitems.all() 
    print(order_items)
    order_total = order_qs[0].get_totals()

    return render(request, 'Payment_App/checkout.html', context={'title':title, 'saved_address':saved_address, 'form':form, 'order_items':order_items, 'order_total':order_total})

@login_required
def payment_view(request):
    saved_address = BillingAddressModel.objects.get_or_create(user=request.user)
    if not saved_address[0].is_fully_filled():
        messages.info(request, f"Please complete shipping address")
        return redirect("Payment_App:checkout")
    
    if not request.user.profile.is_fully_filled():
        messages.info(request, f"Please complete profile details!")
        return redirect("Login_App:profile")
    
    store_id = 'pract657c8e70729e6'
    api_key = 'pract657c8e70729e6@ssl'

    mypayment = SSLCOMMERZ({'store_id': store_id, 'store_pass': api_key, 'issandbox': True})

    status_url = request.build_absolute_uri()
    print("Hello status_url = ", status_url)
    
    mypayment.set_urls(success_url='', fail_url='', cancel_url='', ipn_url='')
    
    status_url = request.build_absolute_uri()
    print(status_url)

    return render(request, "Payment_App/payment.html", context={'title':'Payment'})

@login_required
def complete_view(request):
    render (request, 'Payment_App/complete.html', context={'title':'Complete',})
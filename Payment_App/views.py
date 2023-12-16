from django.shortcuts import render, HttpResponsePermanentRedirect

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
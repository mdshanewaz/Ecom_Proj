from django.shortcuts import render, redirect, get_object_or_404

# Authentications
from django.contrib.auth.decorators import login_required

# Messages
from django.contrib import messages

# Models
from Order_App.models import CartModel, OrderModel
from Shop_App.models import ProductModel

# Create your views here.

@login_required
def add_to_cart_view(request, pk):
    item = get_object_or_404(ProductModel, pk=pk)
    print("item:",item)
    order_item = CartModel.objects.get_or_create(item=item, user=request.user,  purchased=False)
    order_qs = OrderModel.objects.filter(user=request.user, ordered=False)
    print("orderd_item:", order_item)
    print("Order_qs:", order_qs)
    if order_qs.exists():
        order = order_qs[0]
        print("if order exits:", order)
        print("orderd_item:", order_item)
        print("Order_qs:", order_qs)
        print("Order_qs[0]:", order_qs[0])
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "This item quantity was updated")
            return redirect('Shop_App:home')
        else:
            order.orderitems.add(order_item[0])
            messages.info(request, "This item was added to your cart")
            return redirect("Shop_App:home")
    else:
        order = OrderModel(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request, 'This item was added to your cart')
        return redirect('Shop_App:home')
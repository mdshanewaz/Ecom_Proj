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
    order_item = CartModel.objects.get_or_create(item=item, user=request.user, purchased=False)
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


@login_required
def cart_view(request):
    title = 'Your Cart'
    carts = CartModel.objects.filter(user=request.user, purchased=False)
    orders = OrderModel.objects.filter(user=request.user, ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request, 'Order_App/cart.html', context={'title':title, 'carts':carts, 'order':order})
    else:
        messages.warning(request, "You don't have any item in your cart!")
        return redirect('Shop_App:home')

@login_required
def remove_from_cart_view(request, pk):
    item = get_object_or_404(ProductModel, pk=pk)
    order_qs = OrderModel.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = CartModel.objects.filter(item=item, user=request.user, purchased=False)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request, "This item is removed from your cart")
            return redirect("Order_App:cart")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("Shop_App:home")
    else:
        messages.info(request, "You don't have any active order")
        return redirect("Shop_App:home")
    

@login_required
def increase_cart_view(request, pk):
    item = get_object_or_404(ProductModel, pk=pk)
    order_qs = OrderModel.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = CartModel.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                messages.info(request, f"{item.name} quantity has been updated")
                return redirect("Order_App:cart")
        else:
            messages.info(request, f"{item.name} is not in your cart")
            return redirect("Shop_App:home")
    else:
        messages.info(request, "You don't have any active order")
        return redirect("Shop_App:home")
    

@login_required
def decrease_cart_view(request, pk):
    item = get_object_or_404(ProductModel, pk=pk)
    order_qs = OrderModel.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = CartModel.objects.filter(item=item, user=request.user, purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, f"{item.name} quantity has been updated")
                return redirect("Order_App:cart")
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request, f"{item.name} item has been removed from your cart")
                return redirect("Order_App:cart")
        else:
            messages.info(request, f"{item.name} is not in your cart")
            return redirect("Shop_App:home")
    else:
        messages.info(request, "You don't have any active order")
        return redirect("Shop_App:home")
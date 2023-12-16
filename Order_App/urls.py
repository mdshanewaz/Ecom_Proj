from django.urls import path
from Order_App import views


app_name = 'Order_App'

urlpatterns = [
    path('add/<pk>/', views.add_to_cart_view, name='add'),
    path('cart/', views.cart_view, name='cart'),
    path('remove/<pk>/', views.remove_from_cart_view, name='remove'),
    path('increase/<pk>/', views.increase_cart_view, name='increase'),
    path('decrease/<pk>/', views.decrease_cart_view, name='decrease'),
]
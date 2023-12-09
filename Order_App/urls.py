from django.urls import path
from Order_App import views


app_name = 'Order_App'

urlpatterns = [
    path('add/<pk>/', views.add_to_cart_view, name='add'),
    path('cart/', views.cart_view, name='cart'),
]
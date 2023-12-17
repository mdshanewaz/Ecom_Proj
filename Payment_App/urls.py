from django.urls import path
from Payment_App import views


app_name = 'Payment_App'

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path('payment/', views.payment_view, name='payment'),
]
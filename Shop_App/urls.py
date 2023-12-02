from django.urls import path
from Shop_App import views

app_name = 'Shop_App'

urlpatterns = [
    path( '', views.HomeView.as_view(), name='home'),

]
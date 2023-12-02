from django.shortcuts import render, HttpResponseRedirect

# Import views
from django.views.generic import ListView, DetailView

# Models
from Shop_App.models import ProductModel, CategoryModel

# Create your views here.

class HomeView(ListView):
    model = ProductModel
    template_name = 'Shop_App/home.html'
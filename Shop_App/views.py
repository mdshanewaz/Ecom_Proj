from django.shortcuts import render, HttpResponseRedirect

# Mixins
from django.contrib.auth.mixins import LoginRequiredMixin

# Import views
from django.views.generic import ListView, DetailView

# Models
from Shop_App.models import ProductModel, CategoryModel

# Create your views here.

class HomeView(ListView):
    model = ProductModel
    title = "Billing"
    template_name = 'Shop_App/home.html'

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = ProductModel
    template_name = 'Shop_App/product_detail.html'
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
    title = "Home"
    template_name = 'Shop_App/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = ProductModel
    title = "Product Details"
    template_name = 'Shop_App/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context
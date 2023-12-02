from django.contrib import admin
from Shop_App.models import CategoryModel, ProductModel

# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(ProductModel)
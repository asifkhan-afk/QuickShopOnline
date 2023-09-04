from django.contrib import admin
from .models import (Customer,Cart,Product,OrderPlaced)
# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display =["id",'user','name','city','locality','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["id",'title','discount_price']

@admin.register(Cart)
class CartrModelAdmin(admin.ModelAdmin):
    list_display = ["id",'user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ["id"]
from django.contrib import admin

# Register your models here.
from .models import Product, Contact ,Order, OrderUpdates,Service



admin.site.register( Product)
admin.site.register( Contact)
admin.site.register( Order)
admin.site.register( OrderUpdates)

class Services(admin.ModelAdmin):
    list_display =['title','desc']

admin.site.register(Service, Services)

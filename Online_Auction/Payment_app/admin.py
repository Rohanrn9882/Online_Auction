from django.contrib import admin
from .models import *

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'myuser', 'auctiondetails', 'payment_status', 'payment_from', 'payment_to', 'payment_amt']
admin.site.register(Payment, PaymentAdmin)
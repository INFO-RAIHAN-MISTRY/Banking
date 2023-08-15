from django.contrib import admin
from .models import *

# @admin.register(userProfile)
# class profileAdmin(admin.ModelAdmin):
#     list_display = ['phone', 'address', 'country','state','city','pin']

@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'email','aadhar','pan','from_user']

# @admin.register(BankDetails)
# class BankDetailsAdminView(admin.ModelAdmin):
    # list_display = ['customer', 'account_number', 'ifsc_code', 'card_number', 'card_cvv', 'card_pin', 'created_at']
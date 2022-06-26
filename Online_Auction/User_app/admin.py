from django.contrib import admin
from .models import *

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_id', 'country_name', 'country_code']
admin.site.register(Country, CountryAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display = ['state_id', 'country', 'state_name']
admin.site.register(State, StateAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ['city_id', 'state', 'city_name']
admin.site.register(City, CityAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ['area_id', 'city', 'area_name', 'street_name', 'house_no', 'area_pincode']
admin.site.register(Address, AddressAdmin)

class MyUserAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone_number', 'gender', 'is_verified', 'is_admin']
admin.site.register(MyUser, MyUserAdmin)

class IdProofAdmin(admin.ModelAdmin):
    list_display = ['myuser', 'idproof_id', 'idproof_type', 'idproof_image']
admin.site.register(IdProof, IdProofAdmin)
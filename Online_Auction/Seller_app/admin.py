from django.contrib import admin
from .models import *

# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['product_category_id', 'product_category_name']
admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductSubCategoryAdmin(admin.ModelAdmin):
    list_display = ['product_sub_category_id', 'product_category', 'product_sub_category_name']
admin.site.register(ProductSubCategory, ProductSubCategoryAdmin)

class ProductInformationAdmin(admin.ModelAdmin):
    list_display = ['product_info_id', 'product_sub_category', 'myuser', 'product_name', 'product_info_details', 'product_verify', 'product_baseprice', 'is_sold', 'product_location']
admin.site.register(ProductInformation, ProductInformationAdmin)

class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['product_image_id', 'product_information', 'product_image']
admin.site.register(ProductImages, ProductImagesAdmin)
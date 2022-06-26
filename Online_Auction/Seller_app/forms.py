from django import forms
from .models import *

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductSubCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductSubCategory
        fields = '__all__'

class ProductInformationForm(forms.ModelForm):
    class Meta:
        model = ProductInformation
        fields = ['myuser', 'product_sub_category',  'product_info_details', 'product_baseprice', 'product_location']

class ProductImagesForm(forms.ModelForm):
    class Meta:
        model = ProductImages
        fields = '__all__' 
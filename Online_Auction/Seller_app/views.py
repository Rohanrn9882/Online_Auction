from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from .models import *
from .forms import *

# Create your views here.

class ProductView(CreateView):
    model = ProductInformation
    form_class = ProductInformationForm
    template_name = 'Seller_app/productinformation.html'
    success_url = reverse_lazy('showproduct_url')
    def get_context_data(self, *args, **kwargs):
        context = super(ProductView,self).get_context_data(**kwargs)
        context['product_form']=context['form']
        return context
     

class ShowproductView(ListView):
    model = ProductInformation
    template_name = 'Seller_app/showproductinfo.html'

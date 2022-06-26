from django import forms
from .models import *

class SuccessReportForm(forms.ModelForm):
    class Meta:
        model = SuccessReport
        fields = '__all__'

class CancelReportForm(forms.ModelForm):
    class Meta:
        model = CancelReport
        fields = '__all__'

class AuctionQueryForm(forms.ModelForm):
    class Meta:
        model = AuctionQuery
        fields = '__all__'

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'
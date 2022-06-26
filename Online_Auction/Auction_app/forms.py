from django import forms
from .models import *

class AuctionDetailsForm(forms.ModelForm):
    class Meta:
        model = AuctionDetails
        fields = '__all__'

class UserWishlistForm(forms.ModelForm):
    class Meta:
        model = UserWishlist
        fields = '__all__'

class CurrentAuctionForm(forms.ModelForm):
    class Meta:
        model = CurrentAuction
        fields = '__all__'

class BidderForm(forms.ModelForm):
    class Meta:
        model = Bidder
        fields = '__all__'

class AutoBidForm(forms.ModelForm):
    class Meta:
        model = AutoBid
        fields = '__all__'

class SecurityDepositeForm(forms.ModelForm):
    class Meta:
        model = SecurityDeposite
        fields = '__all__'

class CurrentBidForm(forms.ModelForm):
    class Meta:
        model = CurrentBid
        fields = '__all__'

class AllBidForm(forms.ModelForm):
    class Meta:
        model = AllBid
        fields = '__all__'
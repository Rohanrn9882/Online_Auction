from django import forms
from .models import *


gender = [('male','MALE'),('female','FEMALE'),('transgender','TRANSGENDER')]

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['phone_number'].required = True

    class Meta:
        model=MyUser
        fields = ['username','first_name', 'last_name', 'email','phone_number','gender','password','confirm_password', 'is_admin']


        labels = {
            'username':'USERNAME',
            'first_name': 'FIRST NAME',
            'last_name': 'LAST NAME',
            'email': 'EMAIL ID',
            'password':'PASSWORD',
            'confirm_password':'CONFIRM PASSWORD',
            'phone_number': 'CONTACT NUMBER',
            'gender': 'GENDER',
            'is_admin': 'REGISTER AS AUCTIONEER'
        }

        widgets = {
            'username':forms.TextInput(attrs = {
                'placeholder':'username',
                'class' : 'form-control'            }),

            'first_name':forms.TextInput(attrs = {
                'placeholder':'first name',
                'class' : 'form-control'
            }),

            'last_name':forms.TextInput(attrs = {
                'placeholder':'last name',
                'class' : 'form-control'
            }),

            'email':forms.TextInput(attrs = {
                'placeholder':'Enter your Email id',
                'class' : 'form-control'
            }),

            'phone_number':forms.NumberInput(attrs = {
                'placeholder':'Enter Mob.no/Phone.no',
                'class' : 'form-control'
            }),

            'password':forms.TextInput(attrs = {
                'placeholder':'Enter Your Password',
                'class' : 'form-control'
            }),

            'confirm_password':forms.TextInput(attrs = {
                'placeholder':'Confirm Your password',
                'class' : 'form-control'
            }),
            
            'gender': forms.RadioSelect(choices = gender)
        }

    
class IdProofForm(forms.ModelForm):
    class Meta:
        model = IdProof
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    #user_type = forms.CharField(widget=forms.TextInput())
    #profile_photo = forms.ImageField(default='default.jpg', upload_to='/profile_images/' )
    class Meta:
        model = MyUser
        fields = [ 'first_name', 'last_name', 'phone_number', 'profile_photo']

        label ={
            'user_type':'User Type'
        },

        widgets = {
            'user_type':forms.TextInput(attrs = {
                'placeholder': 'Seller/Bidder'
            })
        }
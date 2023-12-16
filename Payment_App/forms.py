from django import forms
from Payment_App.models import BillingAddressModel

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddressModel
        fields = ['address', 'zipcode', 'city', 'country']
        
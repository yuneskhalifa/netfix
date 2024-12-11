from django import forms

from users.models import Company
from .models import Service



class CreateNewService(forms.Form):
    name = forms.CharField(max_length=40)
    description = forms.CharField( label='Description')
    price_hour = forms.DecimalField(
        decimal_places=2, max_digits=5, min_value=0.00)
    
    field = forms.ChoiceField(choices=Service._meta.get_field('field').choices, required=True)
    

    def __init__(self, *args, choices='',visible=True, ** kwargs):
        super(CreateNewService, self).__init__(*args, **kwargs)
        if visible == False:
            self.fields['field'].widget = forms.HiddenInput()
        # adding choices to fields
        if choices:
            self.fields['field'].choices = choices
        # adding placeholders to form fields
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Service Name'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description'
        self.fields['price_hour'].widget.attrs['placeholder'] = 'Enter Price per Hour'

        self.fields['name'].widget.attrs['autocomplete'] = 'off'


from django import forms
from .models import Service, ServiceRequest

class RequestServiceForm(forms.Form):
   
    address = forms.CharField( label="Enter service address", required=True)
    hour = forms.DecimalField(
        decimal_places=2, max_digits=5, min_value=0.00)
    

class RequestServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service', 'address','duration']
        widgets = {
            'service': forms.HiddenInput(),  # Automatically set the service
        }
   
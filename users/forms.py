from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import User, Company, Customer
from .models import Profile

class DateInput(forms.DateInput):
    input_type = 'date'


def validate_email(value):
    # In case the email already exists in an email input in a registration form, this function is fired
    if User.objects.filter(email=value).exists():
        raise ValidationError(
            value + " is already taken.")


class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900,2100)))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()

            #save the customer specific data of birth 
        customer = Customer(user= user, birth=self.cleaned_data['birth_date'])
        customer.save()
        return user


class CompanySignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    field = forms.ChoiceField(
        choices=Company.FIELD_OF_WORK_CHOICES,
        label='Field of Work',
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        if commit:
            user.save()

        # Save Company-specific data (field of work)
        company = Company(user=user, field=self.cleaned_data['field'])
        company.save()
        return user
    


class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(label='Email')  # Replacing username with email
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        # Remove the username field from the form
        del self.fields['username']




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio',]




    

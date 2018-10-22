from django import forms


class UserForm(forms.Form):
    account = forms.CharField(label='account', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='password', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    account = forms.CharField(label='account', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label='name', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='password', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=[('male', 'Male'),
        ('female', 'Female')])
    age = forms.CharField(label='age', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='phone', widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.ChoiceField(choices=[('customer', 'Customer'),
            ('courier', 'Courier')])
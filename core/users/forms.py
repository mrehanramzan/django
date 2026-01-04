from django import forms
from django.contrib.auth import authenticate


class AuthenticateForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput() , max_length=255)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        clean_data = self.cleaned_data
        email = clean_data.get('email')
        password = clean_data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError("Invalid credentials")
        else:
            self.user = user
    
    def get_user(self):
        return self.user
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm

class CustomUserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'username'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'username'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'username'})
        }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if len(username) < 4 or len(password1) < 4:
            raise forms.ValidationError('Username or password Cannot be less than 4 Characters!')
        if password1 != password2:
            raise forms.ValidationError('Password Should be Match!')

        return cleaned_data

class CustomUserloginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'username'}))

class CustomPasswordReset(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'username'}))
    class Meta:
        model = User
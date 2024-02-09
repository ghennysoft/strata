from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone', 'gender', 'birthday', 'profile', 'password']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': "Nom complet"}),
            'email': forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': 'Téléphone'}),
            'gender': forms.Select(attrs={'class': 'form-control p-3'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control p-3', 'placeholder': 'Date de naissance. Format: JJ/MM/AA'}),
            'profile': forms.Select(attrs={'class': 'form-control p-3'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control p-3', 'placeholder': "Mot de passe"}),
        }
        
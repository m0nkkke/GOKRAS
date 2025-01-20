from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import User

class UserRegisterForm(UserCreationForm):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('W', 'Женский'),
    ]

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'user__input', 'placeholder': 'Имя'}),
        label="Имя пользователя",
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'user__input', 'placeholder': 'E-mail'}),
        label="E-mail",
        required=True
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'user__input', 'placeholder': 'Телефон'}),
        label="Телефон",
        required=True
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, label='Пол')
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'user__input', 'placeholder': 'Пароль', 'id': 'password'}),
        label="Пароль"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'user__input', 'placeholder': 'Повторите пароль', 'id': 'password2'}),
        label="Повторите пароль"
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'phone', 'gender', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']  # Имя пользователя
        user.email = self.cleaned_data['email']        # Email пользователя
        user.phone = self.cleaned_data['phone']        # Телефон
        user.gender = self.cleaned_data['gender']      # Пол

        if commit:
            user.save()
        return user
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'user__input',
            'placeholder': 'E-mail'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'user__input',
            'placeholder': 'Пароль',
            'id': 'password'
        })
    )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User  # Убедитесь, что ваша модель пользователя поддерживает поле `photo`
        fields = ['photo']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
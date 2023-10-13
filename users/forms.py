from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User
from main.models import Story


class AddAvatarForm(forms.Form):
    avatar = forms.FileField(label='Добавить файл', widget=forms.FileInput(attrs={
        'class': 'content__input-file',
    }))


class CropAvatarForm(forms.Form):
    hidden = forms.CharField(required=False, widget=forms.HiddenInput(attrs={
        # 'style': 'opacity: 0;position: absolute;z-index: -1;'
    }))


class UserRegisterForm(UserCreationForm):
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'class': 'form__input'
    }))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form__input'
    }))
    surname = forms.CharField(max_length=255, required=False, label='Отчество(если есть)', widget=forms.TextInput(attrs={
        'class': 'form__input'
    }))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form__input'
    }))
    email = forms.EmailField(label='Адрес электронной почты', widget=forms.EmailInput(attrs={
        'class': 'form__input'
    }))
    age = forms.IntegerField(label='Возраст', widget=forms.NumberInput(attrs={
        'class': 'form__input'
    }))
    gender = forms.ChoiceField(label='Пол', choices=User.Gender.choices, widget=forms.Select(attrs={
        'class': 'form__input'
    }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form__input'
    }))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={
        'class': 'form__input'
    }))

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'surname', 'username', 'email', 'age', 'gender', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form__input'
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form__input'
    }))


class NewStoryForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=255, widget=forms.TextInput(attrs={
        'class': 'form__input'
    }))
    body = forms.CharField(label='Содержание', max_length=3000, widget=forms.Textarea(attrs={
        'class': 'form__input',
        'rows': 10,
        'cols': 0
    }))

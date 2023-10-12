from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'Мужской', 'Мужской'
        FEMALE = 'Женский', 'Женский'

    last_name = models.CharField(verbose_name='Фамилия', max_length=150)
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    surname = models.CharField(verbose_name='Отчество', max_length=150, blank=True)
    email = models.EmailField(verbose_name='Адрес электронной почты')
    avatar = models.ImageField(verbose_name='Аватарка', upload_to='images/users/', blank=True, null=True)
    age = models.IntegerField(verbose_name='Возраст', default=7)
    gender = models.CharField(verbose_name='Пол', max_length=7, choices=Gender.choices, default=Gender.MALE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    def get_full_name(self):
        full_name = f'{self.last_name} {self.first_name}'
        if self.surname:
            full_name = f'{full_name} {self.surname}'
        return full_name

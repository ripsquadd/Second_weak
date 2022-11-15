from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=150, verbose_name='Имя', null=False, blank=False)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', null=True, blank=True)
    second_name = models.CharField(max_length=150, verbose_name='Отчество', null=False, blank=False)
    username = models.CharField(max_length=150, verbose_name='Логин', unique=True, null=False, blank=False)
    email = models.CharField(max_length=150, verbose_name='Почта', unique=True, null=False, blank=False)
    password = models.CharField(max_length=150, verbose_name='Пароль', null=False, blank=False)
    personal_data = models.BooleanField(default=False, blank=False, null=False,
                                        verbose_name='Согласие на обработку персональных данных')

    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Прошел активацию?')

    USERNAME_FIELD = 'username'

    class Meta(AbstractUser.Meta):
        pass

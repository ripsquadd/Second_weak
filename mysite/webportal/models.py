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


class Request(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя', blank=False)
    detail = models.CharField(max_length=250, verbose_name='Описание', blank=False)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    photo = models.ImageField(max_length=250, upload_to="img/", blank=False)
    status = models.CharField(max_length=60, verbose_name='Статус',
                              choices=(('new', 'новая'), ('work', 'принято в работу'), ('completed', 'выполнено')),
                              default='new', blank=False)

    def __str__(self):
        return str(self.name) + ' ' + str(self.category)


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя', blank=False)

    def __str__(self):
        return str(self.name)

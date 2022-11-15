from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import User


class RegisterUserForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя',
                           validators=[RegexValidator('^[а-яА-Я- ]+$',
                                                      message='только кирилица и тире')],
                           error_messages={
                               'required': 'Обязательное поле',
                           })

    last_name = forms.CharField(label='Фамилия',
                              validators=[RegexValidator('^[а-яА-Я- ]+$',
                                                         message='только кирилица и тире')],
                              error_messages={
                                  'required': 'Обязательное поле',
                              })

    second_name = forms.CharField(label='Отчество',
                                 validators=[RegexValidator('^[а-яА-Я- ]+$',
                                                            message='только кирилица и тире')],
                                 error_messages={
                                     'required': 'Обязательное поле',
                                 })
    username = forms.CharField(label='Логин',
                               validators=[RegexValidator('^[a-zA-z-]+$',
                                                          message='только латиница и тире')],
                               error_messages={
                                   'required': 'Обязательное поле',
                                   'unique': 'Данный логин занят'
                               })
    email = forms.EmailField(label='Почта',
                             error_messages={
                                 'required': 'Обязательное поле',
                                 'invalid': 'Не правильный формат',
                                 'unique': 'Адрес занят'
                             })
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput,
                               error_messages={
                                   'required': 'Обязательное поле',
                               })
    password2 = forms.CharField(label='Пароль (повторно)',
                                widget=forms.PasswordInput,
                                error_messages={
                                    'required': 'Обязательное поле',
                                })
    personal_data = forms.BooleanField(required=True, label='Согласие на обработку данных',
                                       error_messages={
                                           'required': 'Обязательно поле'
                                       })

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise ValidationError({
                'password2': ValidationError('Пароли не совпадают', code='pass_error')
            })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'second_name', 'username', 'email', 'password', 'password2',
                  'personal_data')

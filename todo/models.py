from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models

class CustomUserCreateForm(UserCreationForm):
    email = forms.EmailField(
        label='Электронная почта',
        required=True,
        help_text='Пожалуйcта, введите ваш email.'
    )
    class Meta:
        model = User
        fields = 'username', 'email'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Придумайте уникальное имя пользователя.'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Этот адрес электронной почты уже используется.')
        return email


class ToDO(models.Model):
    title = models.CharField(max_length=150)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.title


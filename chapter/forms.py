import django.forms

from django import forms
from django.forms import ModelForm
import environ

from .models import ChapterUser, Active, Alumni, Member
env = environ.Env()
environ.Env.read_env()  # reading .env file


class UserForm (forms.ModelForm):
    class Meta:
        model = ChapterUser
        fields = ['first_name', 'last_name', 'email', 'user_state',
                  'user_city', 'pledge_class', 'major', 'username', 'password']


class MemberForm(ModelForm):
    class Meta:
        model = Member
        exclude = ['user', 'paid_dues']


class AlumniUserForm(ModelForm):
    class Meta:
        model = Alumni
        exclude = ['user']

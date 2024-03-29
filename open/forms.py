import django.forms

from django import forms
from django.forms import ModelForm
import environ

from chapter.models import ChapterUser, Active, Alumni
env = environ.Env()
environ.Env.read_env()  # reading .env file


class UserForm (forms.ModelForm):
    class Meta:
        model = ChapterUser
        fields = ['first_name', 'last_name', 'email', 'user_state',
                  'user_city', 'pledge_class', 'major', 'username', 'password']


# Create the form class.
class ActiveUserForm(ModelForm):
    class Meta:
        model = Active
        fields = '__all__'


class AlumniUserForm(ModelForm):
    class Meta:
        model = Alumni
        fields = '__all__'
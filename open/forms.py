import django.forms

from django.forms import ModelForm
from chapter.models import User, Active


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['pledge_class', 'user_city', 'user_state', 'major', 'avatar']


# Create the form class.
class ActiveUserForm(ModelForm):
    class Meta:
        model = Active
        fields = '__all__'


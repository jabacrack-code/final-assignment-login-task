from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'age')
        labels = {
            'username': 'Username',
            'email': 'Mail address',
            'age': 'Age',
        }

class AccountEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'age')

class TaskCreationForm(forms.Form):
    title = forms.CharField(label='タイトル', max_length=255)
    content = forms.CharField(label='内容', widget=forms.Textarea())

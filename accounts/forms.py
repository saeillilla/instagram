from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserAccounts
class Create_New_user(UserCreationForm):
    class Meta:
        model = UserAccounts
        fields = ['email','gender','phone']

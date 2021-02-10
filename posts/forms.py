from django import forms
from .models import Post
class Add_Post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','caption']
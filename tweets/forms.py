from django import forms
from django.core.validators import MaxLengthValidator
from .models import TweetModel


class TweetForm(forms.ModelForm):
    class Meta:
        model = TweetModel
        max_length_validation = forms.IntegerField(validators=[MaxLengthValidator])
        fields = ["content"]

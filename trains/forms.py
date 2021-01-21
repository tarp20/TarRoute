from django import forms

from .models import Train
from cities.models import City

class HtmlForm(forms.Form):
    name = forms.CharField(label='Train')


class TrainForm(forms.ModelForm):

    name = forms.CharField(label='Train Number', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Train Number',
    }))

    travel_time = forms.IntegerField(label='Travel time', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Travel time',
    }))

    city_from = forms.ModelChoiceField(label='From', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}))

    city_to = forms.ModelChoiceField(label='To', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Train
        fields = '__all__'

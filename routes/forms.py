from django import forms

from .models import Route
from cities.models import City


class RouteForm(forms.Form):

    city_from = forms.ModelChoiceField(label='From', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}))

    city_to = forms.ModelChoiceField(label='To', queryset=City.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control js-example-basic-single'}))

    cities = forms.ModelMultipleChoiceField(label='Through The Cities', 
        queryset=City.objects.all(), required=False, widget=forms.SelectMultiple(
        attrs={'class': 'form-control js-example-basic-multiple'}))

    travelling_time = forms.IntegerField(label='Travel time', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Travel time',
    }))

    class Meta:
        model = Route
        fields = '__all__'

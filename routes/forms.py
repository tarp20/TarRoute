from django import forms
from cities.models import City
from routes.models import Route
from trains.models import Train





class RouteForm(forms.Form):
    city_from = forms.ModelChoiceField(
        label='From', queryset=City.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control js-example-basic-single'}
        )
    )
    city_to = forms.ModelChoiceField(
        label='Куда', queryset=City.objects.all(), widget=forms.Select(
            attrs={'class': 'form-control js-example-basic-single'}
        )
    )
    cities = forms.ModelMultipleChoiceField(
        label='throught', queryset=City.objects.all(),
        required=False, widget=forms.SelectMultiple(
            attrs={'class': 'form-control js-example-basic-multiple'}
        )
    )
    travelling_time = forms.IntegerField(
        label='Time Travel', widget=forms.NumberInput(attrs={
            'class': 'form-control', 'placeholder': 'Time Travel'})
    )


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(
        label='Route name', widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter route name'
    }))
    city_from = forms.ModelChoiceField(
        queryset=City.objects.all(), widget=forms.HiddenInput()
    )
    city_to = forms.ModelChoiceField(
        queryset=City.objects.all(), widget=forms.HiddenInput()
    )
    trains = forms.ModelMultipleChoiceField(
        queryset=Train.objects.all(),
        required=False, widget=forms.SelectMultiple(
            attrs={'class': 'form-control d-none'}
        )
    )
    travel_times = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Route
        fields = ('__all__')






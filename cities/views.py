from django.shortcuts import render
from django.views.generic import DetailView

from .models import City



def cities(request,pk=None):
    # if pk:
    #     city = City.objects.filter(id=pk).first()

    #     context = {'object':city}
    #     return render(request, 'cities/detail.html', context)

    qs = City.objects.all()
    context = {'objects_list':qs}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


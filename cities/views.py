from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import City
from .forms import HtmlForm,CityForm



def cities(request,pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()



    # if pk:
    #     city = City.objects.filter(id=pk).first()

    #     context = {'object':city}
    #     return render(request, 'cities/detail.html', context)
    form = CityForm()
    qs = City.objects.all()
    context = {'objects_list':qs,'form':form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(CreateView):

    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities')


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities')

class CityDeleteView(DeleteView):
    model = City
    #template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities')

    def get(self,request,*args,**kwargs):
        return self.post(request,*args,**kwargs)



















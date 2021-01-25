from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import City
from .forms import HtmlForm, CityForm


def cities(request, pk=None):
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
    list = Paginator(qs, 5)
    page_number = request.POST.get('page')
    page_obj = list.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(LoginRequiredMixin,DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):

    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities')
    success_message = 'City created successfully!'


class CityUpdateView(SuccessMessageMixin,LoginRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities')
    success_message = 'City updated successfully!'


class CityDeleteView(LoginRequiredMixin,DeleteView):
    model = City
    #template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'City delated successfully')
        return self.post(request, *args, **kwargs)


class CityListView(LoginRequiredMixin,ListView):
    paginate_by = 5
    model = City
    template_name = 'cities/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm
        context['form'] = form
        return context

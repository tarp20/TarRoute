from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from django.core.paginator import Paginator

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Train
# from .forms import HtmlForm, TrainForm


def trains(request, pk=None):

    qs = Train.objects.all()
    list = Paginator(qs, 5)
    page_number = request.POST.get('page')
    page_obj = list.get_page(page_number)
    context = {'page_obj': page_obj,}
    return render(request, 'trains/home.html', context)


class TrainListView(ListView):
    paginate_by = 5
    model = Train
    template_name = 'trains/home.html'



class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'


# class CityCreateView(SuccessMessageMixin, CreateView):

#     model = Train
#     form_class = TrainForm
#     template_name = 'trains/create.html'
#     success_url = reverse_lazy('trains')
#     success_message = 'Train created successfully!'


# class CityUpdateView(SuccessMessageMixin, UpdateView):
#     model = Train
#     form_class = TrainForm
#     template_name = 'trains/update.html'
#     success_url = reverse_lazy('trains')
#     success_message = 'Train updated successfully!'


# class CityDeleteView(DeleteView):
#     model = Train
#     #template_name = 'trains/delete.html'
#     success_url = reverse_lazy('trains')

#     def get(self, request, *args, **kwargs):
#         messages.success(request, 'Train delated successfully')
#         return self.post(request, *args, **kwargs)

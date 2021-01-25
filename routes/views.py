from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


from .forms import RouteForm, RouteModelForm
from .utils import get_routes
from .models import Route
from trains.models import Train
from cities.models import City



def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})


def find_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', context)
        return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, 'No Search Data')
        return render(request, 'routes/home.html', {'form': form})


def add_route(request):
    if request.method == 'POST':
        context = {}
        form = RouteModelForm(request.POST)
        data = request.POST
        context['form'] = form
        if data:
            total_time = int(data['total_time'])
            city_from_id = int(data['city_from'])
            city_to_id = int(data['city_to'])
            trains = data['trains'].split(',')
            trains_lst = [int(t) for t in trains if t.isdigit()]
            qs = Train.objects.filter(id__in=trains_lst).select_related(
                'city_from', 'city_to')
            cities = City.objects.filter(
                id__in=[city_from_id, city_to_id]).in_bulk()
            form = RouteModelForm(
                initial={
                    'city_from': cities[city_from_id],
                    'city_to': cities[city_to_id],
                    'travel_times': total_time,
                    'trains': qs
                         }
            )
            context['form'] = form

        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, 'Impossible to save a non-existent route')
        return redirect('/')


def save_route(request):
    if request.method == 'POST':
        context = {}
        form = RouteModelForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'The route saved successfully')
            return redirect('/')

        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, 'Impossible to save a non-existent route')
        return redirect('/')


class RouteListView(ListView):
    paginate_by = 10
    model = Route
    template_name = 'routes/list.html'


class RouteDetailView(DetailView):
    queryset = Route.objects.all()
    template_name = 'routes/detail.html'


class RouteDeleteView(LoginRequiredMixin, DeleteView):
    model = Route
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Route deleted successfully')
        return self.post(request, *args, **kwargs)





from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .forms import RouteForm, RouteModelForm
from .utils import get_routes


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
            messages.error(request, 'The route saved successfully')
            return redirect('/')

        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, 'Impossible to save a non-existent route')
        return redirect('/')

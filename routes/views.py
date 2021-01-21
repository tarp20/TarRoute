from django.shortcuts import render
from django.contrib import messages

from .forms import RouteForm



def home(request):
    form = RouteForm()
    return render(request,'routes/home.html',{'form':form})




def find_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            
        return render(request,'routes/home.html',{'form':form})
    else:
        form = RouteForm()
        messages.error(request,'No Search Data')
        return render(request,'routes/home.html',{'form':form})


from django.contrib import admin
from django.urls import path,include
from cities.views import cities

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/',include('cities.urls')),
    path('trains/',include('trains.urls')),
    path('', cities , name = 'home')
]

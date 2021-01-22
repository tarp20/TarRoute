
from django.contrib import admin
from django.urls import path,include
from routes.views import home,find_route,add_route,save_route

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/',include('cities.urls')),
    path('trains/',include('trains.urls')),
    path('', home , name = 'home'),
    path('find_route/', find_route,name = 'find_route'),
    path('add_route/', add_route,name = 'add_route'),
    path('save_route/', save_route,name = 'save_route'),

]

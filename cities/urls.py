from django.urls import path
from .views import cities,CityDetailView,CityCreateView,CityUpdateView,CityDeleteView

urlpatterns = [
    path('', cities, name='cities'),
    path('detail/<int:pk>/', CityDetailView.as_view(),name='detail'),
    path('add/',CityCreateView.as_view(),name='new_city'),
    path('update/<int:pk>/',CityUpdateView.as_view(),name = 'update_city'),
    path('delete/<int:pk>/',CityDeleteView.as_view(),name = 'delete_city')


]

from django.urls import path
from .views import cities, CityDetailView, CityCreateView,CityUpdateView, CityDeleteView, CityListView

urlpatterns = [
    #  path('', cities, name='cities'),
    path('', CityListView.as_view(), name='cities'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='city_detail'),
    path('add/', CityCreateView.as_view(), name='city_add'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='city_udpate'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='city_delete')


]

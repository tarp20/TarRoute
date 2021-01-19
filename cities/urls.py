from django.urls import path
from .views import cities,CityDetailView

urlpatterns = [
    path('', cities, name='cities'),
    path('detail/<int:pk>/', CityDetailView.as_view(),name='detail')
]

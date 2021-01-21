from django.urls import path
from .views import trains, TrainListView, TrainDetailView , TrainCreateView,TrainUpdateView, TrainDeleteView

urlpatterns = [
    #  path('', trains, name='trains'),
    path('', TrainListView.as_view(), name='trains'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='train_detail'),
    path('add/', TrainCreateView.as_view(), name='train_add'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='train_udpate'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='train_delete'),


]

from django.urls import path
from . import views

urlpatterns = [
    path('api/dogs', views.DogList.as_view(), name='dogs_list'),
    path('api/dogs/<int:pk>', views.DogDetail.as_view(), name='dog_detail'),
]

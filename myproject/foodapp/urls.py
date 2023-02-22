from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addFoodView, name='add'),
    path('menu/',views.showDetailsView, name='show'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addFoodView, name='add'),
    path('menu/',views.showDetailsView, name='show'),
    path('edit/', views.editDetailsView, name='edit'),
    path('up/<int:id>',views.updateDetailsView, name='update'),
    path('del/<int:id>', views.deleteDetailsView, name='delete'),
]
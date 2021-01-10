from django.urls import path
from .import views

urlpatterns = [
    path('', views.show_projects, name='show_projects'),
    path('rating/', views.add_rating, name='add_rating'),
]

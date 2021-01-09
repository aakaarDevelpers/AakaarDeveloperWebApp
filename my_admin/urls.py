from django.urls import path
from .import views

urlpatterns = [
    path('', views.my_admin_homepage, name='admin_home'),
    path('delete/<str:id>/', views.delete_blog, name='delete_blog'),
]

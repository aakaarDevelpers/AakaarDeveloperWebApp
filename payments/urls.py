from django.urls import path
from .import views

urlpatterns = [
    path('', views.payment_index, name='payment_method'),
]

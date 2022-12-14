from django.urls import path
from .import views
from django.views.decorators.csrf import csrf_exempt #to desable the csrf checking

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
]
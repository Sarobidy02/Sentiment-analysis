from django.urls import path
from .import views
from django.views.decorators.csrf import csrf_exempt #to desable the csrf checking

urlpatterns = [
    path('', views.PredicitonView.as_view(), name = 'prediction'),
    path('score', csrf_exempt(views.Score.as_view()), name = 'score')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.GrowView.as_view(), name='grow'),
    ]
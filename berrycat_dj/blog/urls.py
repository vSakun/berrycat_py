from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('article/', views.article, name='article'),
    path('search/', views.search, name='search'),
    path('rubric/', views.rubric, name='rubric'),
]

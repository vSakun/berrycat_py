from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='blog-home'),
    path('post/<int:id>/', views.DetailArticleView.as_view(), name='post'),
    path('search/', views.search, name='search'),
    path('articles/', views.AllArticleView.as_view(), name='articles'),
    path('articles/travel/', views.TravelArticleView.as_view(), name='travel'),
    path('articles/hand_made/', views.HandMadeArticleView.as_view(), name='hand_made'),
    path('articles/coffee_country/',
         views.HandMadeArticleView.as_view(), name='coffee_country'),
    path('articles/places_and_events/',
         views.HandMadeArticleView.as_view(), name='places_and_events'),
]

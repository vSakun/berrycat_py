from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='blog-home'),
    path('articles/<int:pk>/', views.DetailArticleView.as_view(), name='article'),
    path('user/<str:username>/', views.UserArticleView.as_view(), name='user_article_view'),
    path('search/', views.SearchArticleView.as_view(), name='search'),
    path('articles/', views.AllArticleView.as_view(), name='articles'),
    path('articles/travel/', views.TravelArticleView.as_view(), name='travel'),
    path('articles/hand_made/', views.HandMadeArticleView.as_view(), name='hand_made'),
    path('articles/coffee_country/',
         views.Coffee_CountryArticleView.as_view(), name='coffee_country'),
    path('articles/places_and_events/',
         views.Places_and_EventsArticleView .as_view(), name='places_and_events'),
]

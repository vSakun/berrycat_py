from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:id>/', views.DetailArticleView.as_view(), name='post'),
    path('search/', views.search, name='search'),
    path('articles/', views.AllArticleView.as_view(), name='articles'),
]

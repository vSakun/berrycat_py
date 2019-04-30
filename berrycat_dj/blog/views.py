from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    return render(request, 'blog/index.html')


def article(request):
    return render(request, 'blog/article.html')

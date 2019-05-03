from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    return render(request, 'blog/index.html')


def article(request):
    return render(request, 'blog/article.html')


def search(request):
    return render(request, 'blog/search.html')


def rubric(request):
    return render(request, 'blog/rubric.html')

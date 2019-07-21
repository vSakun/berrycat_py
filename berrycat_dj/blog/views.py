from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
# from django.http import HttpResponse


def home(request):
    # data = {
    #     'article': Article.objects.all(),
    # }
    return render(request, 'blog/index.html')


def post(request):
    return render(request, 'blog/article.html')


def search(request):
    return render(request, 'blog/search.html')


# def rubric(request):
#     return render(request, 'blog/rubric.html')

class AllArticleView(ListView):
    queryset = Article.objects.filter(active=1)
    template_name = 'blog/rubric.html'
    context_object_name = 'article'
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        ctx = super(AllArticleView, self).get_context_data(**kwargs)
        ctx['page_title'] = 'Статьи'
        return ctx


class TravelArticleView(ListView):
    template_name = 'blog/rubric.html'
    context_object_name = 'article'
    ordering = ['-date']
    queryset = Article.objects.filter(rubric='travel', active=1)

    def get_context_data(self, **kwargs):
        ctx = super(TravelArticleView, self).get_context_data(**kwargs)
        ctx['page_title'] = 'путешествия'
        return ctx


class HandMadeArticleView(ListView):
    template_name = 'blog/rubric.html'
    context_object_name = 'article'
    ordering = ['-date']
    queryset = Article.objects.filter(rubric='hand_made', active=1)

    def get_context_data(self, **kwargs):
        ctx = super(HandMadeArticleView, self).get_context_data(**kwargs)
        ctx['page_title'] = 'HAND MADE'
        return ctx


class Coffee_CountryArticleView(ListView):
    template_name = 'blog/rubric.html'
    context_object_name = 'article'
    ordering = ['-date']
    queryset = Article.objects.filter(rubric='coffee_country', active=1)

    def get_context_data(self, **kwargs):
        ctx = super(Coffee_CountryArticleView, self).get_context_data(**kwargs)
        ctx['page_title'] = 'Страна кофе'
        return ctx


class Places_and_EventsArticleView(ListView):
    template_name = 'blog/rubric.html'
    context_object_name = 'article'
    ordering = ['-date']
    queryset = Article.objects.filter(rubric='places_and_events', active=1)

    def get_context_data(self, **kwargs):
        ctx = super(Places_and_EventsArticleView,
                    self).get_context_data(**kwargs)
        ctx['page_title'] = 'Места и события'
        return ctx


class DetailArticleView(DetailView):
    model = Article

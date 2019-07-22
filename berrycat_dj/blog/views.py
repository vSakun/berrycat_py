from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
from random import randint
# from django.http import HttpResponse


class HomeView(ListView):
    # model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article'

    # def get_context_data(self, **kwargs):
    #     ctx = super(HomeView, self).get_context_data(**kwargs)
    #     ctx['page_title'] = 'BerryCat'
    #     return ctx

    def get_queryset(self):

        random_index = randint(0, Article.objects.count() - 4)

        big_best_article = Article.objects.filter(
            active=1).order_by('-like')[0]
        small_best_article = Article.objects.filter(
            active=1).order_by('-like')[1:5]
        last_article = Article.objects.filter(
            active=1).order_by('-date')[:9]
        gallery_article = Article.objects.filter(
            active=1).order_by('-date')[5:10]
        random_article = Article.objects.filter(
            active=1)[random_index:random_index + 4]
        data = {
            'big_best_article': big_best_article,
            'small_best_article': small_best_article,
            'last_article': last_article,
            'gallery_article': gallery_article,
            'random_article': random_article
        }
        return data
    # def get_context_data(self, **kwargs):
    #     ctx = super(HomeView, self).get_context_data(**kwargs)
    #     ctx['big_best_article'] = Article.objects.filter(
    #         active=1).order_by('-like')[0]
    #     ctx['small_best_article'] = Article.objects.filter(
    #         active=1).order_by('-like')[1:5]
    #     ctx['last_article'] = Article.objects.filter(
    #         active=1).order_by('-date')[:5]
    #     return ctx


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
    template_name = 'blog/article_detail.html'

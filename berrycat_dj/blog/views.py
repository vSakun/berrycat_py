from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
#from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView
from .models import Article, CommentArticle
from random import randint
from .forms import CommentForm
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class HomeView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article'


    def get_queryset(self):

        random_index = randint(0, Article.objects.count() - 4)

        big_view_article = Article.objects.filter(
            active=1).order_by('-views_all')[0]
        small_view_article = Article.objects.filter(
            active=1).order_by('-views_all')[1:5]
        last_article = Article.objects.filter(
            active=1).order_by('-date')[:9]
        gallery_article = Article.objects.filter(
            active=1).order_by('-date')[5:10]
        random_article = Article.objects.filter(
            active=1)[random_index:random_index + 4]
        data = {
            'big_view_article': big_view_article,
            'small_view_article': small_view_article,
            'last_article': last_article,
            'gallery_article': gallery_article,
            'random_article': random_article
        }
        return data

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['title'] = 'BarryCat'
        return ctx

def search(request):
    return render(request, 'blog/search.html')

class UserArticleView(ListView):
    model = Article
    template_name = 'blog/search.html'
    context_object_name = 'article'
    ordering = ['-date']
    paginate_by = 9

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Article.objects.filter(active=1, avtor=user)

    def get_context_data(self, **kwargs):
        random_index = randint(0, Article.objects.count() - 3)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        ctx = super(UserArticleView, self).get_context_data(**kwargs)
        ctx['title'] = 'Статьи ' + str(user)
        ctx['best_article'] = Article.objects.filter(
            active=1).order_by('-like')[random_index:random_index + 3]
        return ctx

class SearchArticleView(ListView):
    model = Article
    template_name = 'blog/search.html'
    context_object_name = 'article'
    ordering = ['-date']
    # paginate_by = 9

    def get_context_data(self, **kwargs):
        ctx = super(SearchArticleView, self).get_context_data(**kwargs)
        random_index = randint(0, Article.objects.count() - 3)

        question = self.request.GET.get('q')
        if question is not None:
            search_articles = Article.objects.filter(Q(text_article__icontains=question) | Q(text_preview__icontains=question) | Q(title__icontains=question))
            ctx['article'] = search_articles
            ctx['title'] = 'Поиск: ' + question
            ctx['best_article'] = Article.objects.filter(active=1).order_by('-like')[random_index:random_index + 3]
            ctx['question'] = question
        return ctx

class AllArticleView(ListView):
    queryset = Article.objects.filter(active=1)
    template_name = 'blog/rubric.html'
    context_object_name = 'article'
    ordering = ['-date']
    paginate_by = 9

    def get_context_data(self, **kwargs):
        ctx = super(AllArticleView, self).get_context_data(**kwargs)
        ctx['title'] = 'Статьи'
        return ctx


class TravelArticleView(ListView):
    template_name = 'blog/rubric.html'
    context_object_name = 'article'
    ordering = ['-date']
    queryset = Article.objects.filter(rubric='travel', active=1)
    paginate_by = 9

    def get_context_data(self, **kwargs):
        ctx = super(TravelArticleView, self).get_context_data(**kwargs)
        ctx['title'] = 'Путешествия'
        return ctx


class HandMadeArticleView(ListView):
    template_name = 'blog/rubric.html'
    context_object_name = 'article'
    ordering = ['-date']
    queryset = Article.objects.filter(rubric='hand_made', active=1)
    paginate_by = 9

    def get_context_data(self, **kwargs):
        ctx = super(HandMadeArticleView, self).get_context_data(**kwargs)
        ctx['title'] = 'HAND MADE'
        return ctx


class Coffee_CountryArticleView(ListView):
    template_name = 'blog/rubric.html'
    context_object_name = 'article'
    ordering = ['-date']
    queryset = Article.objects.filter(rubric='coffee_country', active=1)
    paginate_by = 9

    def get_context_data(self, **kwargs):
        ctx = super(Coffee_CountryArticleView, self).get_context_data(**kwargs)
        ctx['title'] = 'Страна кофе'
        return ctx


class Places_and_EventsArticleView(ListView):
    template_name = 'blog/rubric.html'
    context_object_name = 'article'
    ordering = ['-date']
    queryset = Article.objects.filter(rubric='places_and_events', active=1)
    paginate_by = 9

    def get_context_data(self, **kwargs):
        ctx = super(Places_and_EventsArticleView,
                    self).get_context_data(**kwargs)
        ctx['title'] = 'Места и события'
        return ctx


class DetailArticleView(DetailView, UpdateView):
    model = Article
    form_class = CommentForm
    template_name = 'blog/article_detail.html'

    def get_context_data(self, **kwargs):
        random_index = randint(0, Article.objects.count() - 3)
        id_article = get_object_or_404(Article, pk=self.kwargs['pk'])
        id_article.views_all += 1
        id_article.save(update_fields=['views_all'])
        ctx = super(DetailArticleView, self).get_context_data(**kwargs)
        ctx['form'] = CommentForm()
        ctx['comments'] = CommentArticle.objects.filter(
            for_article=id_article, active=True)
        ctx['best_article'] = Article.objects.filter(
            active=1).order_by('-like')[random_index:random_index + 3]
        ctx['title'] = Article.objects.filter(pk=self.kwargs['pk']).first()
        return ctx

    def form_valid(self, form):
        form.save()
        avtor_comment = form.cleaned_data['avtor_comment']
        text_comment = form.cleaned_data['text_comment']
        for_article = Article.objects.filter(pk=self.kwargs['pk']).first()
        comment = CommentArticle.objects.create(
            avtor_comment=avtor_comment, text_comment=text_comment, for_article=for_article)
        comment.save()
        return self.render_to_response(self.get_context_data(form=form))

def likedislike(request):
    if request.GET:
        key_ldl = request.GET.get('ldl')
        title = request.GET.get('title')
        article = get_object_or_404(Article, title=title)
        if key_ldl == 'like':
            article.like += 1
            article.save(update_fields=['like'])
            data = {'key_ldl': article.like}
            return JsonResponse(data)
        elif key_ldl =='dislike':
            article.dislike += 1
            article.save(update_fields=['dislike'])
            data = {'key_ldl': article.dislike}
            return JsonResponse(data)
        else:
            return JsonResponse('What?')
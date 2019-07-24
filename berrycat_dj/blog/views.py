from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView
from .models import Article, CommentArticle
from random import randint
from .forms import CommentForm
from django.http import HttpResponseRedirect


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
        ctx['title'] = 'Статьи'
        return ctx


class TravelArticleView(ListView):
    template_name = 'blog/rubric.html'
    context_object_name = 'article'
    ordering = ['-date']
    queryset = Article.objects.filter(rubric='travel', active=1)

    def get_context_data(self, **kwargs):
        ctx = super(TravelArticleView, self).get_context_data(**kwargs)
        ctx['title'] = 'путешествия'
        return ctx


class HandMadeArticleView(ListView):
    template_name = 'blog/rubric.html'
    context_object_name = 'article'
    ordering = ['-date']
    queryset = Article.objects.filter(rubric='hand_made', active=1)

    def get_context_data(self, **kwargs):
        ctx = super(HandMadeArticleView, self).get_context_data(**kwargs)
        ctx['title'] = 'HAND MADE'
        return ctx


class Coffee_CountryArticleView(ListView):
    template_name = 'blog/rubric.html'
    context_object_name = 'article'
    ordering = ['-date']
    queryset = Article.objects.filter(rubric='coffee_country', active=1)

    def get_context_data(self, **kwargs):
        ctx = super(Coffee_CountryArticleView, self).get_context_data(**kwargs)
        ctx['title'] = 'Страна кофе'
        return ctx


class Places_and_EventsArticleView(ListView):
    template_name = 'blog/rubric.html'
    context_object_name = 'article'
    ordering = ['-date']
    queryset = Article.objects.filter(rubric='places_and_events', active=1)

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
        # print(self.get_success_url())
        # return HttpResponseRedirect(self.get_success_url())

# def comments(request, pk):
#     article = get_object_or_404(CommentArticle, id=pk)
#     print(article)
#     comment = CommentArticle.objects.filter(for_article=article, active=True)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comm = form.save(commit=False)
#             comm.avtor_comment = request.avtor_comment
#             comm.article = article
#             comm.save()
#             return redirect('article', slug=post.slug)
#     else:
#         form = CommentForm()

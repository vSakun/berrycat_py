from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(Article)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'rubric', 'date']

    class Meta:
        model = models.Article


class CommentArticleAdmin(admin.ModelAdmin):
    list_display = ['avtor_comment', 'for_article', 'date_created', 'active']

    class Meta:
        model = models.CommentArticle


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.CommentArticle, CommentArticleAdmin)

from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(Article)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'active', 'rubric', 'date']

    class Meta:
        model = models.Article


admin.site.register(models.Article, ArticleAdmin)

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here


class Article(models.Model):

    RUBRIC = (
        ('all', "Статьи"),
        ('travel', "Путешествия"),
        ('coffee_country', "Страна Кофе"),
        ('hand_made', "Hand made"),
        ('places_and_events', "Места и события")
    )

    active = models.BooleanField()
    rubric = models.CharField(
        max_length=100, choices=RUBRIC, verbose_name="Рубрика", default="all")
    title = models.CharField(max_length=100, verbose_name="Название статьи")
    text_article = RichTextField()
    text_preview = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    avtor = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BigIntegerField()
    dislike = models.BigIntegerField()
    views_all = models.BigIntegerField()
    image = models.ImageField(upload_to='pictures/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class CommentArticle(models.Model):
    class Meta():
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    avtor_comment = models.CharField(max_length=255)
    for_article = models.ForeignKey(
        Article, verbose_name="Статья", on_delete=models.CASCADE)
    text_comment = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

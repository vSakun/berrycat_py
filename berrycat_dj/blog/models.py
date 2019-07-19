from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here


class Article(models.Model):
    active = models.BooleanField()
    title = models.CharField(max_length=100)
    text_article = RichTextField()
    text_preview = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    avtor = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BigIntegerField()
    dislike = models.BigIntegerField()
    views_all = models.BigIntegerField()
    image = models.ImageField(upload_to='pictures/', null=True, blank=True)

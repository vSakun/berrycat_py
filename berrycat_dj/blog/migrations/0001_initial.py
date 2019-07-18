# Generated by Django 2.2 on 2019-07-18 14:25

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('title', models.CharField(max_length=100)),
                ('text_article', ckeditor.fields.RichTextField()),
                ('text_preview', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('like', models.BigIntegerField()),
                ('dislike', models.BigIntegerField()),
                ('views_all', models.BigIntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('avtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
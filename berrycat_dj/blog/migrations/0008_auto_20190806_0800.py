# Generated by Django 2.2 on 2019-08-06 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_commentarticle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='views_all',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]

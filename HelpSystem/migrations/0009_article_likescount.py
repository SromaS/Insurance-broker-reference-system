# Generated by Django 3.0.2 on 2020-03-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelpSystem', '0008_remove_article_likescount'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='likesCount',
            field=models.IntegerField(null=True, verbose_name='Количество лайков'),
        ),
    ]
# Generated by Django 3.0.2 on 2020-03-24 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HelpSystem', '0006_auto_20200324_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='likes_count',
            new_name='likesCount',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='views_count',
            new_name='viewsCount',
        ),
    ]

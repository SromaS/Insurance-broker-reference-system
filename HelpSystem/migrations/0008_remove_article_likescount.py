# Generated by Django 3.0.2 on 2020-03-24 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HelpSystem', '0007_auto_20200324_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='likesCount',
        ),
    ]

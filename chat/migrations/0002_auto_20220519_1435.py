# Generated by Django 3.2 on 2022-05-19 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='chat_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

# Generated by Django 3.2 on 2022-05-20 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_message_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='chat_images'),
        ),
    ]

# Generated by Django 4.1.1 on 2023-02-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crcikblogs', '0023_memes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='memes',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='memes',
            name='image',
            field=models.ImageField(upload_to='meme/'),
        ),
    ]

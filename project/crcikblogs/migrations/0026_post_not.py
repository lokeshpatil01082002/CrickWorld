# Generated by Django 4.1.1 on 2023-02-16 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crcikblogs', '0025_meme_likes_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='post_not',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.IntegerField()),
                ('userid', models.CharField(max_length=30)),
            ],
        ),
    ]
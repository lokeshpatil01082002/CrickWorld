# Generated by Django 4.1.1 on 2023-02-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crcikblogs', '0026_post_not'),
    ]

    operations = [
        migrations.CreateModel(
            name='meme_not',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('meme_id', models.IntegerField()),
                ('userid', models.CharField(max_length=30)),
            ],
        ),
    ]

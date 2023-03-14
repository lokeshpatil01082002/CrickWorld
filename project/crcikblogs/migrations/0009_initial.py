# Generated by Django 4.1.1 on 2023-02-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crcikblogs', '0008_delete_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('userid', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('reward', models.IntegerField()),
            ],
        ),
    ]

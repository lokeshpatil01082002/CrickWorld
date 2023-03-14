# Generated by Django 4.1.1 on 2023-02-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crcikblogs', '0014_delete_userdetails_delete_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('userid', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('reward', models.IntegerField()),
            ],
        ),
    ]

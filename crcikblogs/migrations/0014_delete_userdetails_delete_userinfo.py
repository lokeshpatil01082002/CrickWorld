# Generated by Django 4.1.1 on 2023-02-11 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crcikblogs', '0013_alter_userdetails_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserDetails',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]

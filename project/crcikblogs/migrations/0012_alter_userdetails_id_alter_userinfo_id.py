# Generated by Django 4.1.1 on 2023-02-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crcikblogs', '0011_alter_userinfo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
# Generated by Django 4.1.1 on 2023-02-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crcikblogs', '0012_alter_userdetails_id_alter_userinfo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-03 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='user',
            name='date_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='date update'),
        ),
    ]

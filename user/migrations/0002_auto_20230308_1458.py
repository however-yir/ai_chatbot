# Generated by Django 3.2.8 on 2023-03-08 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='1', max_length=50, verbose_name='昵称'),
        ),
    ]

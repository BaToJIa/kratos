# Generated by Django 4.1.3 on 2023-03-26 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kratos_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processor',
            name='Сокет',
        ),
        migrations.AddField(
            model_name='processor',
            name='Сокет',
            field=models.ManyToManyField(null=True, to='kratos_app.socket'),
        ),
    ]

# Generated by Django 4.1.3 on 2023-03-27 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kratos_app', '0006_rename_name_socket_socket_socket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producer',
            old_name='name_producer',
            new_name='producer',
        ),
    ]

# Generated by Django 4.1.3 on 2023-03-27 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kratos_app', '0007_rename_name_producer_producer_producer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producer',
            old_name='producer',
            new_name='name_producer',
        ),
    ]

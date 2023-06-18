# Generated by Django 4.1.3 on 2023-03-26 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kratos_app', '0003_alter_processor_frequency_alter_ram_frequency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='motherboard',
            name='image_motherboard',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='processor',
            name='image_processor',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='ram',
            name='image_ram',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='videocard',
            name='image_videocard',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

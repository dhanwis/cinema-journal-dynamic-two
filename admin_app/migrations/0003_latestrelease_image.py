# Generated by Django 5.0.1 on 2024-02-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_remove_latestrelease_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestrelease',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='admin_app/latestrelease'),
        ),
    ]

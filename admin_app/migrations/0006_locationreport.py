# Generated by Django 5.0.1 on 2024-02-14 06:04

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0005_latestrelease_author_latestrelease_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date', models.DateField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('text', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
            ],
        ),
    ]
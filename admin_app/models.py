from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class LatestRelease(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    text = CKEditor5Field('Text', config_name='extends')
    
class LocationReport(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    text = CKEditor5Field('Text', config_name='extends')
    
class MeetThePerson(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    text = CKEditor5Field('Text', config_name='extends')

class TeaserAndPromose(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    text = CKEditor5Field('Text', config_name='extends')
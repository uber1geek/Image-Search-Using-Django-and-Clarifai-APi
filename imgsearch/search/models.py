from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager


# Create your models here.

class Image(models.Model):
    image_url = models.CharField(max_length=512, null = True, blank = True)
    tags = TaggableManager()

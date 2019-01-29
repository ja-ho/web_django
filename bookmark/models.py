from __future__ import unicode_literals # Python2.x 지원용

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.contrib.auth.models import User
# Create your models here.

@python_2_unicode_compatible			# python2.x 지원용
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class T_USER(models.Model):
    user_id = models.CharField(max_length=8,primary_key=True)
    user_name = models.CharField(max_length=20)
    user_password= models.CharField(max_length=100)
    user_status=models.CharField(max_length=1)
    def __unicode__(self):
        return self.user_name
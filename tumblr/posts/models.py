from django.db import models
from datetime import datetime
# Create your models here.

#post id, post date, post content

#migration: something you have to do whenever you alter the structure of the database (new models, fields, etc)
#1. create migration: list out steps for SQL to do in order to restructure database
#2. run migration: actually restructure

class Post(models.Model):
    #id, date, content, description, tags
    post_id = models.CharField(default='', max_length=200)
    title = models.CharField(default='', max_length=200)
    time = models.DateTimeField(default=datetime.now, blank=True)
    content = models.TextField()
    description = models.CharField(default='',max_length=200)
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Person(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Blog(models.Model):

    name = models.CharField('Blog',max_length=250)
    tag_line = models.TextField('Tag line')

    def __unicode__(self):
        return self.name

class Author(models.Model):

    name = models.CharField('Author',max_length=200)
    email = models.EmailField('Email')

    def __unicode__(self):
        return self.name

class Entry(models.Model):

    Blog = models.ForeignKey(Blog,on_delete=models.CASCADE,verbose_name='Blog')
    authors = models.ManyToManyField(Author,verbose_name='Authors')
    headline = models.CharField('HeadLine',max_length=250)

    

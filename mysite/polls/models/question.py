from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.question_text

    def execute_function(self):
        self.pub_date = timezone.now()

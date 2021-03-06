from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

# what Django will do?
# 1. create a database schema
# 2. create a python database access api
# python manage.py makemigrations dashboard
# to see what has happened: python manage.py sqlmigrate dashboard 0001
# python manage.py migrate to do the real migrate work.
@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days = 1) <= self.pub_date <= timezone.now()

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
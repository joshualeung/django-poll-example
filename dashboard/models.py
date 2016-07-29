from __future__ import unicode_literals

from django.db import models

# Create your models here.

# what Django will do?
# 1. create a database schema
# 2. create a python database access api
# python manage.py makemigrations dashboard
# to see what has happened: python manage.py sqlmigrate dashboard 0001
# python manage.py migrate to do the real migrate work.

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
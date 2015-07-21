# -*- coding: utf-8 -*-
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    checked = models.BooleanField(default=False)


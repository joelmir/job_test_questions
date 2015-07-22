# -*- coding: utf-8 -*-
from django.db import models
from questions.models import Question, Choice

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

class Answer(models.Model):
    '''
      Have Question and Answer, to know what questions existed
      when the candidate answer the test and his option is none
    '''
    candidate = models.ForeignKey(Candidate)
    question = models.ForeignKey(Question)
    choice = models.ForeignKey(Choice, blank=True, null=True)



# -*- coding: utf-8 -*-
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __unicode__(self):
      return u'{0}'.format(self.question_text)

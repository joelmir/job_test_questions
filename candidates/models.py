# -*- coding: utf-8 -*-
from django.db import models
from questions.models import Question
from django.core.mail import send_mail

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __unicode__(self):
      return u'{0} - {1}'.format(self.name, self.email)

    def send_email(self):
        send_mail('Subject here', 'Enviar email' , 'joelmir.ribacki@gmail.com',['joedekid@gmail.com'], fail_silently=False)
    


class Answer(models.Model):
    candidate = models.ForeignKey(Candidate)
    question = models.ForeignKey(Question)
    grade = models.IntegerField()

    def __unicode__(self):
      return u'{0} - {1} - {2}'.format(self.candidate.name, self.question, self.grade)



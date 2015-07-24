# -*- coding: utf-8 -*-
from django.db import models
from questions.models import Question
from django.core.mail import send_mail

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __unicode__(self):
      return u'{0} - {1}'.format(self.name, self.email)

    def send_mail(self):
        questions_id = Answer.objects.filter(candidate=self, grade__gte=7).values_list('question_id')
        questions = [question.lower().strip() for question in Question.objects.filter(id__in=questions_id).values_list('question_text', flat=True)]
        default_mail = True
        if 'html' in questions and 'css' in questions and 'javascript' in questions:
            default_mail = False
            print 'Front-End'
            send_mail('Obrigado por se candidatar', '''Obrigado por se candidatar, assim que tivermos uma vaga disponível

para programador Front-End entraremos em contato.''' , 'joelmir.ribacki@gmail.com',[self.email], fail_silently=False)

        if 'python' in questions and 'django' in questions:
            default_mail = False
            print 'Back-End'
            send_mail('Obrigado por se candidatar', '''Obrigado por se candidatar, assim que tivermos uma vaga disponível

para programador Back-End entraremos em contato.''' , 'joelmir.ribacki@gmail.com',[self.email], fail_silently=False)
        
        if 'desenvolvedor ios' in questions or 'desenvolvedor android' in questions:
            default_mail = False
            print 'Mobile'
            send_mail('Obrigado por se candidatar', '''Obrigado por se candidatar, assim que tivermos uma vaga disponível

para programador Mobile entraremos em contato.''' , 'joelmir.ribacki@gmail.com',[self.email], fail_silently=False)

        if default_mail:
            print 'Default: ', self.email
            send_mail('Obrigado por se candidatar', '''Obrigado por se candidatar, assim que tivermos uma vaga disponível

para programador entraremos em contato.''' , 'joelmir.ribacki@gmail.com',[self.email], fail_silently=False)


class Answer(models.Model):
    candidate = models.ForeignKey(Candidate)
    question = models.ForeignKey(Question)
    grade = models.IntegerField()

    def __unicode__(self):
      return u'{0} - {1} - {2}'.format(self.candidate.name, self.question, self.grade)



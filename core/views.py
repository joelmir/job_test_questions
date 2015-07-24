from django.shortcuts import render
from questions.models import Question
from django.core.mail import send_mail

def home(request):

    #send_mail('Subject here', 'Here is the message.', 'joelmir.ribacki@gmail.com',['joedekid@gmail.com'], fail_silently=False)
    return render(request, 'index.html', { 
      'questions':Question.objects.all().order_by('question_text')
    })
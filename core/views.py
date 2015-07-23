from django.shortcuts import render
from questions.models import Question

def home(request):

  return render(request, 'index.html', { 
      'questions':Question.objects.all().order_by('question_text')
    })
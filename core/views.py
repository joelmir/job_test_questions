from django.shortcuts import render
from questions.models import Question
from django.core.mail import send_mail
from candidates.models import Candidate, Answer

def home(request):
    if request.method == 'GET':
        return render(request, 'index.html', { 
          'questions':Question.objects.all().order_by('question_text')
        })
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        candidate = Candidate.objects.create(name=name, email=email)
        
        for option in [key for key in request.POST.keys() if 'slider' in key]:
            question_id = option.split('-')[1]
            if not request.POST.has_key('disable-{0}'.format(question_id)):
                question = Question.objects.get(id=question_id)
                Answer.objects.create(candidate=candidate, question=question, grade=int(request.POST.get(option)))

        return render(request, 'index.html', { 
          'questions':Question.objects.all().order_by('question_text')
        })





        #send_mail('Subject here', , 'joelmir.ribacki@gmail.com',['joedekid@gmail.com'], fail_silently=False)
    
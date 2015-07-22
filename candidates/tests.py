# -*- coding: utf-8 -*-
from django.test import TestCase

from candidates.models import Candidate, Answer
from questions.models import Question, Choice

class CandidateTestCase(TestCase):
    def setUp(self):
        Candidate.objects.create(name="João", email='joao@gmail.com')
        Candidate.objects.create(name="Anastacia", email='anastacia@gmail.com')
        question1 = Question.objects.create(question_text="First question")
        Choice.objects.create(question=question1, choice_text='Option 1')

    def test_candidate_can_have_answes(self):
        """Choices can add to a Question correctly """
        question1 = Question.objects.get(question_text="First question")
        choice1 = Choice.objects.get(question=question1)
        joao = Candidate.objects.get(email="joao@gmail.com")
        
        Answer.objects.create(candidate=joao, choice=choice1, question=question1)
        self.assertEqual(Answer.objects.get(candidate=joao).choice, choice1)

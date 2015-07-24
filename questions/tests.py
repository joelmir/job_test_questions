# -*- coding: utf-8 -*-
from django.test import TestCase
from questions.models import Question

class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(question_text="First question")

    def test_question_can_be_removed(self):
        """Can be remove one question """
        question1 = Question.objects.get(question_text="First question")
        question1.delete()
        self.assertEqual(len(Question.objects.all()), 0)



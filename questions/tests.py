# -*- coding: utf-8 -*-
from django.test import TestCase
from questions.models import Question

# class QuestionTestCase(TestCase):
#     def setUp(self):
#         Question.objects.create(question_text="First question")
#         Question.objects.create(question_text="Other question")

#     def test_question_can_have_choices(self):
#         """Choices can add to a Question correctly """
#         question1 = Question.objects.get(question_text="First question")
#         Choice.objects.create(question=question1, choice_text='Option 1')
#         self.assertEqual(Choice.objects.get(choice_text='Option 1').question, question1)

#     def test_question_can_have_two_choices(self):
#         """Choices can add to a Question correctly """
#         question1 = Question.objects.get(question_text="First question")
#         Choice.objects.create(question=question1, choice_text='Option 1')
#         Choice.objects.create(question=question1, choice_text='Option 2')
#         self.assertEqual(len(Choice.objects.filter(question=question1)), 2)

#     def test_question_can_remove_option(self):
#         """Choices can add to a Question correctly """
#         question1 = Question.objects.get(question_text="First question")
#         option_to_remove = Choice.objects.create(question=question1, choice_text='Option 1')
#         Choice.objects.create(question=question1, choice_text='Option 2')
#         option_to_remove.delete()
#         self.assertEqual(len(Choice.objects.filter(question=question1)), 1)



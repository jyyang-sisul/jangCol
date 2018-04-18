# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

import datetime

from django.utils import timezone

from blog.models import Question

class QuestionMethodTests(TestCase):
        
        
    """
    def test_was_published_recently_with_future_question(self):
        
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
    """    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now    
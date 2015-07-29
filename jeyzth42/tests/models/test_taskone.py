# -*- coding: utf-8 -*-
"""Test suite for the TG app's models"""
from __future__ import unicode_literals
from nose.tools import eq_

from jeyzth42 import model
from jeyzth42.tests.models import ModelTest


class TestTaskOne:
   """Unit test case for the ``TaskOne`` model."""
   
   klass = model.TaskOne
   attrs = dict(
       name="Tester",
       lastname="SurTester",
       dateofbird="28.07.2015",
       bio="""
          What does field may be consist?\n
          My biografy? It take many words.\n
          Biological kind? Homo sapiens.\nOther variants.
          """,
       email="tester.taskone@yahoo.com",
       skype="tester.taskone",
       jabber="tester@xmpp.jp",
       othr="""
       phone + 1 333 12345678
       mobile +1 909 65432110
       fax +1 929 67189016
       """,
   )
   
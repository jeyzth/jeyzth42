# -*- coding: utf-8 -*-
"""Test suite for the TG app's models"""
from __future__ import unicode_literals
from nose.tools import eq_

from jeyzth42 import model
from jeyzth42.tests.models import ModelTest


class TestGroup(ModelTest):
    """Unit test case for the ``Group`` model."""

    klass = model.Group
    attrs = dict(
        group_name="test_group",
        display_name="Test Group"
    )


class TestUser(ModelTest):
    """Unit test case for the ``User`` model."""

    klass = model.User
    attrs = dict(
        user_name="ignucius",
        email_address="ignucius@example.org"
    )

    def test_obj_creation_username(self):
        """The obj constructor must set the user name right"""
        eq_(self.obj.user_name, "ignucius")

    def test_obj_creation_email(self):
        """The obj constructor must set the email right"""
        eq_(self.obj.email_address, "ignucius@example.org")

    def test_no_permissions_by_default(self):
        """User objects should have no permission by default."""
        eq_(len(self.obj.permissions), 0)

    def test_getting_by_email(self):
        """Users should be fetcheable by their email addresses"""
        him = model.User.by_email_address("ignucius@example.org")
        eq_(him._id, self.obj._id)


class TestPermission(ModelTest):
    """Unit test case for the ``Permission`` model."""

    klass = model.Permission
    attrs = dict(
        permission_name="test_permission",
        description="This is a test Description"
    )

class TestTaskOne:
   """Unit test case for the ``TaskOne`` model."""
   
   klass = model.TaskOne
   attrs = dict(
       name="Tester",
       lastname="SurTester",
       dateofbird="28.07.2015"
       bio=""" What does field may be consist?
       My biografy? It take many words.
       Biological kind? Homo sapiens.
       Other variants&
       """
       email="tester.taskone@yahoo.com"
       skype="tester.taskone"
       jabber="tester@xmpp.jp"
       othr="""
       phone + 1 333 12345678
       mobile +1 909 65432110
       fax +1 929 67189016
       """
   )
   
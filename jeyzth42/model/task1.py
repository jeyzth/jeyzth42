# -*- coding: utf-8 -*-
"""
Task1* related model.

This is where the models used by the authentication stack are defined.

It's perfectly fine to re-use this definition in the jeyzth42 application,
though.

"""
import os
from datetime import datetime
from hashlib import sha256
__all__ = ['TaskOne']

from ming import schema as s

from ming.odm import FieldProperty, ForeignIdProperty, RelationProperty
from ming.odm import Mapper
from ming.odm.declarative import MappedClass
from jeyzth42.model import DBSession


class TaskOne(MappedClass):
    """
    Colection TaskOne  definition.
    """
    class __mongometa__:
        session = DBSession
        name = 'tg_taskone'
        unique_indexes = [('name',),]

    _id = FieldProperty(s.ObjectId)
    name = FieldProperty(s.String)
    lastname = FieldProperty(s.String)
    dateofbird = FieldProperty(s.String)
    Bio = FieldProperty(s.String)
    email = FieldProperty(s.String)
    jabber = FieldProperty(s.String)
    skype = FieldProperty(s.String)
    othr = FieldProperty(s.String)


#!/usr/bin/python
from ming import Session
from ming import create_datastore
from ming.odm import ThreadLocalODMSession

bind = create_datastore('jeyzth42')
doc_session = Session(bind)
session = ThreadLocalODMSession(doc_session=doc_session)



from ming import schema
from ming.odm import FieldProperty, ForeignIdProperty, RelationProperty
from ming.odm import Mapper
from ming.odm.declarative import MappedClass

class TaskOne(MappedClass):
    
    class __mongometa__:
        session = session
        name = 'tg_taskone'
                       
    _id = FieldProperty(schema.ObjectId)
    name = FieldProperty(str)
    lastname = FieldProperty(str)
    dataofbird = FieldProperty(str)
    bio =  FieldProperty(str)
                                    
Mapper.compile_all()
                                        
ListOfPeople = TaskOne.query.get(name=u'Evgen');
print("name="+ListOfPeople['name'])
print("lastname="+ListOfPeople['lastname'])
print("Date of bird="+ListOfPeople['dateofbird'])
print("Bio:\n"+ListOfPeople['bio'])
print("email="+ListOfPeople['email'])
print("jid="+ListOfPeople['jid'])
print("skype="+ListOfPeople['skype'])
print("Other information:\n"+ListOfPeople['othr'])
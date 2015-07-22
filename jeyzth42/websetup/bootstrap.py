# -*- coding: utf-8 -*-
"""Setup the jeyzth42 application"""
from __future__ import print_function
from jeyzth42 import model


def bootstrap(command, conf, vars):
    """Place any commands to setup jeyzth42 here"""
    # <websetup.bootstrap.before.auth
    
        g = model.Group()
        g.group_name = 'managers'
        g.display_name = 'Managers Group'

        p = model.Permission()
        p.permission_name = 'manage'
        p.description = 'This permission gives an administrative right'
        p.groups = [g]

        u = model.User()
        u.user_name = 'manager'
        u.display_name = 'Example manager'
        u.email_address = 'manager@somedomain.com'
        u.groups = [g]
        u.password = 'managepass'

        u1 = model.User()
        u1.user_name = 'editor'
        u1.display_name = 'Example editor'
        u1.email_address = 'editor@somedomain.com'
        u1.password = 'editpass'  
    
        t1 = model.TaskOne()
        t1.name = 'Evgen'
        t1.lastname = 'Anonimov'
        t1.dateofbird='01.01.1973'
        t1.bio="""I like cats, but don't like dogs. """
        t1.email='jeyzth@gmail.com'
        t1.jabber='jeyzth@xmpp.jp'
        t1.skype='jeyzth'
        t1.othr="Phones 717123456 Mobile +77011234567"
    
    model.DBSession.flush()
    model.DBSession.clear()

    # <websetup.bootstrap.after.auth>

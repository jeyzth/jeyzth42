# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from jeyzth42 import model
from jeyzth42.controllers.secure import SecureController
from tgext.admin.mongo import BootstrapTGMongoAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from jeyzth42.lib.base import BaseController
from jeyzth42.controllers.error import ErrorController
from jeyzth42.model.task1 import TaskOne
__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the jeyzth42 application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
#    secc = SecureController()
#    admin = AdminController(model, None, config_type=TGAdminConfig)
#    error = ErrorController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "jeyzth42"

    @expose('jeyzth42.templates.index')
    def index(self):
        """Handle the front-page."""
        t1=TaskOne.query.get(name=u'Evgen');
        
        return dict(title='This is may first page Jinja.',page='index.html',name=t1.name,lastname=t1.lastname,
           dateofbird=t1.dateofbird,bio=t1.bio,email=t1.email,skype=t1.skype, jabber=t1.jabber,othr=t1.othr)
        


# -*- coding: utf-8 -*-

#  Quickstarted Options:
#
#  sqlalchemy: False
#  auth:       ming
#  mako:       False
#
#

# This is just a work-around for a Python2.7 issue causing
# interpreter crash at exit when trying to log an info message.
try:
    import logging
    import multiprocessing
except:
    pass

import sys
py_version = sys.version_info[:2]

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

testpkgs = [
    'WebTest >= 1.2.3',
    'nose',
    'coverage',
    'gearbox'
]

install_requires = [
    "TurboGears2 >= 2.3.5",
    "Babel",
    "Genshi",
    "ming>=0.4.3",
    "repoze.who",
    "tw2.forms",
    "tgext.admin >= 0.6.1",
]
if py_version == (3, 2):
    # jinja2 2.7 is incompatible with Python 3.2
    install_requires.append('jinja2 < 2.7')
else:
    install_requires.append('jinja2')

setup(
    name='jeyzth42',
    version='0.1',
    description='',
    author='',
    author_email='',
    url='',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=testpkgs,
    package_data={'jeyzth42': [
        'i18n/*/LC_MESSAGES/*.mo',
        'templates/*/*',
        'public/*/*'
    ]},
    message_extractors={'jeyzth42': [
        ('**.py', 'python', None),
        ('templates/**.html', 'genshi', None),
        ('public/**', 'ignore', None)
    ]},
    entry_points={
        'paste.app_factory': [
            'main = jeyzth42.config.middleware:make_app'
        ],
        'gearbox.plugins': [
            'turbogears-devtools = tg.devtools'
        ]
    },
    zip_safe=False
)

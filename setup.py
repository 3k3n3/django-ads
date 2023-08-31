# -*- coding: utf-8 -*-
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

from ads import __version__


here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# This fork is based on the following versions
REQUIREMENTS = [
    'Django>=4.2',
    'django-appconf>=1.0.5',
    'django-sekizai>=4.1.0',
    'django-braces>=1.15.0',
    'django-js-reverse>=0.10.2',
    'Pillow',
]


CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='django-ads',
    version=__version__,
    description='Ads Management System for Django Framework',
    long_description=long_description,
    author='Razi Alsayyed',
    author_email='razi.sayed@gmail.com',
    url='https://github.com/razisayyed/django-ads',
    packages=find_packages(),
    license='LICENSE',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False
)

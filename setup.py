#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from setuptools import setup

import os
import re

def abs_path(relative_path):
    """
    Given a path relative to this directory return an absolute path.
    """
    base_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(base_path, relative_path)

def get_version(relative_path):
    """
    Return version given package's path.
    """
    data = open(os.path.join(abs_path(relative_path), '__init__.py')).read()
    return re.search(r"__version__ = '([^']+)'", data).group(1)

def get_long_description():
    """
    Return the contents of the README file.
    """
    try:
        return open(abs_path('README.rst')).read()
    except:
        pass # Required to install using pip (won't have README.rst then)


setup(
    name='django-selenium-client',
    version=get_version('django_selenium_client'),
    description='A Django Test Client that runs a live server instance.',
    long_description=get_long_description(),
    author='Bright Interactive',
    packages=('django_selenium_client',),
    package_dir={'django_selenium_client': 'django_selenium_client'},
)

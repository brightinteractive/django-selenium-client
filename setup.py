#!/usr/bin/env/python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="djangoseleniumclient",
    version="0.1",
    description="A Django Test Client that runs a live server instance"
                " as required for full-browser testing.",
    author='Bright Interactive',
    packages=('djangoseleniumclient',),
    package_dir={'djangoseleniumclient': 'djangoseleniumclient'},
)

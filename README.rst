Django Selenium Client
======================

A Django Test Client class that fires up a live server so that
full UI tests such as Selenium tests may be run.

Based on this outstanding ticket in Django: https://code.djangoproject.com/ticket/2879

Small modification was made in testserver.py

Slightly tweaked TestServerThread to get database settings since the settings
as they were have since been deprecated.

Usage
-----

from django_selenium_client import SeleniumTestCase

TODO:

1. Doc import'ing this
2. Doc usage more throughly
3. Get selenium settings from settings.py

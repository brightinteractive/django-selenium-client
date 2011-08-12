Django Selenium Client
======================

A Django Test Client class that fires up a live server so that
full UI tests such as Selenium tests may be run.

Based on this outstanding ticket in Django: https://code.djangoproject.com/ticket/2879

Small modification was made in testserver.py

Slightly tweaked TestServerThread to get database settings since the settings
as they were have since been deprecated.

Installation
------------

Follow the GitHub setup instructions.

Install using pip::

    pip install git+ssh://git@github.com/brightinteractive/django-selenium-client.git


Usage
-----

In ``settings.py``::

    TEST_SERVER_HOSTNAME = '0.0.0.0'   # Network-visible, unlike 127.0.0.1
    TEST_SERVER_PORT = 8001
    
    SELENIUM_HOSTNAME = 'plumpton' 
    SELENIUM_PORT = 4444
    SELENIUM_BROWSER = '*chrome'  # Weirdly, this doesn't actually mean chrome.


In your app's ``tests.py`` file::

    from django_selenium_client import SeleniumTestCase

    class ExampleTests(SeleniumTestCase):
        def test_example(self):
            self.selenium.open('/example')

TODO
----

Get selenium settings from settings.py

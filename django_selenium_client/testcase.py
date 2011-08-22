import socket

from django.conf import settings
from django.test import TestCase

from .testserver import TestServerThread
from .selenium import selenium


class UITestCase(TestCase):
    """
    TestCase that adds support for starting and stopping a live test server.
    """

    def start_test_server(self,
                          address=settings.TEST_SERVER_HOSTNAME,
                          port=settings.TEST_SERVER_PORT): 
        """
        Creates a live test server object (instance of WSGIServer).
        """ 
        self.server_thread = TestServerThread(address, port) 
        self.server_thread.start() 
        self.server_thread.started.wait()

        if self.server_thread.error:
            raise self.server_thread.error 

    def stop_test_server(self):
        """
        Pull down the test server.
        """
        if self.server_thread: 
            self.server_thread.join()


class SeleniumTestCase(UITestCase):
    def setUp(self): 
        """
        Start a test server and tell selenium where to find it.
        """
        # Usually socket.gethostbyname(socket.gethostname()) will return an
        # IP address of the machine that it is run on, but sometimes it
        # doesn't work (e.g. if the machine is not connected to a network),
        # therefore we support an optional HOSTNAME_AS_SEEN_BY_SELENIUM
        # setting.
        hostname = getattr(settings, 'HOSTNAME_AS_SEEN_BY_SELENIUM', None)
        if hostname is None:
            hostname = socket.gethostbyname(socket.gethostname())
        self.TEST_SERVER_URL = 'http://%s:%d' % (hostname,
                                                 settings.TEST_SERVER_PORT)

        self.start_test_server(settings.TEST_SERVER_HOSTNAME,
                               settings.TEST_SERVER_PORT)
        self.selenium = selenium(settings.SELENIUM_HOSTNAME,
                                 settings.SELENIUM_PORT,
                                 settings.SELENIUM_BROWSER,
                                 self.TEST_SERVER_URL)
        self.selenium.start()

    def tearDown(self):
        """
        Stop server and Selenium.
        """
        self.selenium.stop()
        self.stop_test_server()

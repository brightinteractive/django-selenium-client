from django.test import TestCase
from testserver import TestServerThread
from selenium import selenium


class UITestCase(TestCase):
    """
    TestCase that adds support for starting and stopping a live test server.
    """

    def start_test_server(self, address='localhost', port=8001): 
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
        self.start_test_server('localhost', 8001)
        self.selenium = selenium('localhost', 4444,
                                 '*pifirefox', 'http://localhost:8001') 

    def tearDown(self):
        """
        Stop server and Selenium.
        """
        self.selenium.stop()
        self.stop_test_server()

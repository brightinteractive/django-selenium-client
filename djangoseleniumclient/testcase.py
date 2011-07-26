from django.test import TestCase
from testserver import TestServerThread
from selenium import selenium
import socket


TEST_SERVER_HOSTNAME = '0.0.0.0'   # Network-visible, unlike 127.0.0.1
TEST_SERVER_PORT = 8001

SELENIUM_HOSTNAME = 'plumpton' 
SELENIUM_PORT = 4444

# See: http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
LOCAL_IP_ADDR = socket.gethostbyname(socket.gethostname())
TEST_SERVER_URL = 'http://%s:%d' % (LOCAL_IP_ADDR, TEST_SERVER_PORT)

class UITestCase(TestCase):
    """
    TestCase that adds support for starting and stopping a live test server.
    """

    def start_test_server(self, address=TEST_SERVER_HOSTNAME, port=TEST_SERVER_PORT): 
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
        self.start_test_server(TEST_SERVER_HOSTNAME, TEST_SERVER_PORT)
        self.selenium = selenium(SELENIUM_HOSTNAME, SELENIUM_PORT,
                                 '*pifirefox', TEST_SERVER_URL) 

    def tearDown(self):
        """
        Stop server and Selenium.
        """
        self.selenium.stop()
        self.stop_test_server()

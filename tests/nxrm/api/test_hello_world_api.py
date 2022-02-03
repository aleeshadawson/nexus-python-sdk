import unittest
from nexus.nxrm.api.hello_world_api import HelloWorldApi

class HelloWorldApiTest(unittest.TestCase):
    def test_hello(self):
        api = HelloWorldApi()
        self.assertEquals(api.hello(), 'Hello World')

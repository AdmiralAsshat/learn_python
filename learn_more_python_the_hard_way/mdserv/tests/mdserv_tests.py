from nose.tools import *
from mdserv import blog
import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        blog.app.config['TESTING'] = True
        self.app = blog.app.test_client()

    def test_index(self):
        page = self.app.get('/')
        assert_true('Welcome to LAME BLOG' in page.data)

    def test_mdfile(self):
        page = self.app.get('/foo.html')
        assert_true('snap' in page.data)

if __name__ == '__main__':
    unittest.main()
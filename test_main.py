import unittest
from main import app


class TestCases(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        pass

    def tearDown(self):
        dummy = 1

    def test_dummy(self):
        r = self.app.get('/')
        print('status_code=%s' % r.status_code)
        assert r.status_code == 200


if __name__ == '__main__':
    unittest.main()

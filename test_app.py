# -*- coding: utf-8 -*-

import unittest
import webtest
import app


class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.myapp = webtest.TestApp(app.app)

    def test_app_index(self):
        resp = self.myapp.get('/')
        assert resp.status_code == 200
        assert 'Hello World!' in resp.body.decode("utf-8")

    def test_page_not_found(self):
        try:
            self.myapp.get('/doesnt_exist')
        except webtest.app.AppError as err:
            assert '404 Not Found' in err.args[0]

if __name__ == '__main__':
    unittest.main()

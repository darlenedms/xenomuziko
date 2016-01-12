# -*- coding: utf-8 -*-

import unittest
import webtest
import app


class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.myapp = webtest.TestApp(app.app)

    def test_index(self):
        resp = self.myapp.get('/')

        self.assertEqual(resp.status_code, 200)
        self.assertNotEqual(
            resp.html.find('input', attrs={'name': 'username'}), None)

    def test_result_page(self):
        resp = self.myapp.post('/result', {'username': 'yada'})

        self.assertEqual(resp.status_code, 200)
        self.assertNotEqual(resp.text.find('yada'), -1)

    def test_page_not_found(self):
        try:
            self.myapp.get('/doesnt_exist')
        except webtest.app.AppError as err:
            assert '404 Not Found' in err.args[0]

if __name__ == '__main__':
    unittest.main()

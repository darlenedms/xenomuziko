# -*- coding: utf-8 -*-

import unittest
import app


class TestHomePage(unittest.TestCase):

    def test_app_index(self):
        assert app.index() == 'Hello World!'

if __name__ == '__main__':
    unittest.main()

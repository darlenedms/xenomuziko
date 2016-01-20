# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch, Mock
import lastfm
import json


class TestLastFm(unittest.TestCase):

    @patch('lastfm.urllib3.poolmanager.PoolManager.request')
    def test_get_top_artists(self, mock_request):
        mock_response = Mock()

        with open('tests/fixtures/fake_get_top_artists.json') as data_file:
            expected_dict = json.load(data_file)

        mock_response.data.decode.return_value = json.dumps(expected_dict)
        mock_request.return_value = mock_response

        response_dict = lastfm.get_top_artists('Gashash')

        self.assertEqual(1, mock_response.data.decode.call_count)
        self.assertEqual(response_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-

import os
import json
import urllib3


def get_top_artists(user):
    http = urllib3.PoolManager()

    params = {'method': 'user.gettopartists',
              'user': user,
              'api_key': os.environ.get('LASTFM_API_KEY'),
              'format': 'json'}

    url = 'http://ws.audioscrobbler.com/2.0/'
    resp = http.request('GET', url, params)
    http.clear()

    data = json.loads(resp.data.decode('utf-8'))
    return data

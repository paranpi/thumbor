#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import time
import tornado.httpclient
import tornado.ioloop
from thumbor import __version__


class ErrorHandler(object):
    def __init__(self, config):
        self.url = "https://hooks.slack.com/services/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"

    def stop_server(self, response):
        ioloop = tornado.ioloop.IOLoop.instance()
        ioloop.add_callback(ioloop.stop)

    def handle_error(self, context, handler, exception):
        req = handler.request
        extra = {
            'thumbor-version': __version__,
            'timestamp': time.time()
        }

        extra.update({
            'Headers': req.headers
        })

        cookies_header = extra.get('Headers', {}).get('Cookie', {})
        if isinstance(cookies_header, basestring):
            cookies = {}
            for cookie in cookies_header.split(';'):
                if not cookie:
                    continue
                values = cookie.strip().split('=')
                key, val = values[0], "".join(values[1:])
                cookies[key] = val
        else:
            cookies = cookies_header

        extra['Headers']['Cookie'] = cookies
        extra['Headers'] = extra['Headers'].items()

        data = {
            'Http': {
                'url': req.full_url(),
                'method': req.method,
                'data': req.arguments,
                'body': req.body,
                'query_string': req.query
            },
            'interfaces.User': {
                'ip': req.remote_ip,
            },
            'exception': str(exception),
            'extra': extra
        }

        payload = {
            "channel": "@chris", "username": "thumbor-error", "text": json.dumps(data), "icon_emoji": ":exclamation:"
        }
        client = tornado.httpclient.AsyncHTTPClient()
        req = tornado.httpclient.HTTPRequest(
            url=self.url,
            method="POST",
            body=json.dumps(payload)
        )
        client.fetch(req, callback=self.stop_server)

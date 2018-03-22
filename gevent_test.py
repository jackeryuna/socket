'''import json
import random

from gevent import pywsgi, sleep
from geventwebsocket.handler import WebSocketHandler

class WebSocketApp(object):

    def __call__(self, environ, start_response):
        ws = environ['wsgi.websocket']
        x = 0
        while True:
            data = json.dumps({'x': x, 'y': random.randint(1, 5)})
            ws.send(data)
            x += 1
            sleep(0.5)


server = pywsgi.WSGIServer(("", 10000), WebSocketApp(), handler_class=WebSocketHandler)
server.serve_forever()'''
from gevent.pywsgi import WSGIServer

def application(environ, start_response):
    status = '200 OK'

    headers = [
        ('Content-Type', 'text/html')
    ]

    start_response(status, headers)
    yield "<p> Hello".encode()
    yield "World</p>".encode()

WSGIServer(('', 8000), application).serve_forever()
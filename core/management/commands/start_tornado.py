#coding: utf-8

import sys
import base64
import StringIO

# Import 3rd-party modules.
from tornado import websocket, web, ioloop
import numpy
from streams import ws

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'starts tornado server'

    def handle(self, *args, **options):
	app = web.Application([
	    (r'/', ws.IndexHandler),
	    (r'/ws', ws.SocketHandler),
	])

        app.listen(9002)
        ioloop.IOLoop.instance().start()

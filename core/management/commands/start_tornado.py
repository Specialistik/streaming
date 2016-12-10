#coding: utf-8

import sys
import base64
import StringIO

# Import 3rd-party modules.
from tornado import websocket, web, ioloop
import numpy
import coils

from django.core.management.base import BaseCommand
from streams.ws import start_tornado


class Command(BaseCommand):
    help = 'starts tornado server'

    def handle(self, *args, **options):
	app = web.Application([
	    (r'/cuck', IndexHandler),
	    (r'/', SocketHandler),
	])

        app.listen(9002)
        ioloop.IOLoop.instance().start()

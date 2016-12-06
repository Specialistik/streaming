#coding: utf-8

from tornado import web
from tornadio2 import SocketConnection, TornadioRouter, SocketServer

class WSConnection(SocketConnection):
    def on_message(self, msg):
	print 'message received'

    def on_open(self, args):
	print 'connection established'

    def on_close(self):
	print 'connection closed'


def start_tornado(port):
    router = TornadioRouter(WSConnection)
    app = web.Application(router.urls, socket_io_port = port)
    SocketServer(app)


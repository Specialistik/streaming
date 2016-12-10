
# Import standard modules.
import sys
import base64
import StringIO

# Import 3rd-party modules.
from tornado import websocket, web, ioloop
import numpy
import coils


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render('index.html')

class SocketHandler(websocket.WebSocketHandler):
    def __init__(self, *args, **kwargs):
        super(SocketHandler, self).__init__(*args, **kwargs)

        # Client to the socket server.
        self._map_client = coils.MapSockClient('127.0.0.1', 9002, encode=False)

        # Monitor the framerate at 1s, 5s, 10s intervals.
        self._fps = coils.RateTicker((1,5,10))

    def on_message(self, message):
        response = self._map_client.send(coils.MapSockRequest('get', 'image'))
        sio = StringIO.StringIO(response)
        image = numpy.load(sio)
        image = base64.b64encode(image)
        self.write_message(image)

        # Print object ID and the framerate.
        text = '{} {:.2f}, {:.2f}, {:.2f} fps'.format(id(self), *self._fps.tick())
        print(text)



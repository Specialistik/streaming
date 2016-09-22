#!/usr/bin/env python

import os
#import ffmpy
#import vimeo
from flask import Flask, render_template, Response
from camera import VideoCamera
from converter import Converter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder='static')
video_factory = Converter()


def convert(video):
    video_factory.thumbnail(video, 10, BASE_DIR + video.split('.')[0] + '.png', '320x320')
    return os.path.join('static', 'mp4', video)


@app.context_processor
def inject_videos():
    result_list = []
    for filename in os.listdir(os.path.join(BASE_DIR, 'static', 'mp4')):
        result_list.append(filename)
    return {'videos': result_list}


@app.route('/')
def index():
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    inject_videos()
    app.run(host='0.0.0.0', debug=True)

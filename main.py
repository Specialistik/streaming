#!/usr/bin/env python

import os
import cv2
from flask import Flask, render_template, Response
from camera import VideoCamera
from werkzeug.contrib.fixers import ProxyFix

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder='static')
app.config.from_object('config')


def convert(video_file):
    uri = os.path.join(BASE_DIR, 'static/mp4', video_file)
    cap = cv2.VideoCapture(uri)
    count = 0

    while cap.isOpened():
        count += 1
        ret, frame = cap.read()

        if count > 300:
            dirty_file_name = video_file.split('.')[0]
            thumbnail_uri = dirty_file_name + '.png'
            cv2.imwrite(os.path.join(BASE_DIR, 'static', 'thumbs', thumbnail_uri), frame)
            return {
                'pic_url': '/static/thumbs/' + thumbnail_uri,
                'pic_href': '/static/mp4/' + dirty_file_name + '.mp4'
            }

    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()
    return False


def thumbnail(video_file):
    dirty_file_name = video_file.split('.')[0]
    thumbnail_uri = dirty_file_name + '.png'
    return {
        'pic_url': '/static/thumbs/' + thumbnail_uri,
        'pic_href': '/static/mp4/' + dirty_file_name + '.mp4'
    }

@app.context_processor
def inject_videos():
    result_list = []
    for filename in os.listdir(os.path.join(BASE_DIR, 'static', 'mp4')):
        result_list.append(thumbnail(filename))
    return {'videos': result_list}


@app.route('/')
def index():
    return render_template('main_page.html')


@app.route('/subcategory')
def category():
    return render_template('subcategory.html')


@app.route('/author')
def author():
    return render_template('author.html')


@app.route('/video_storage')
def video_storage():
    return render_template('left.html')


@app.route('/streaming')
def streaming():
    return render_template('right.html')

@app.route('/up')
def up():
    return render_template('top.html')

@app.route('/down')
def down():
    return render_template('bottom.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    inject_videos()
    app.run(host='0.0.0.0', debug=True)

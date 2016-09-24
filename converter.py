import os
from converter import Converter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def convert(video_file):
    c = Converter()
    c.thumbnail(BASE_DIRvideo_file, 10, '../thumbs/' + video_file, '320x320')


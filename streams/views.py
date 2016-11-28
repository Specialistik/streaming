#coding: utf-8

from django.shortcuts import render
from streams.models import AudioStream, VideoStream, VideoStreamSet

def audio_stream(request, id):
    return render(request, 'audio_stream.html', {'audio_stream': AudioStream.objects.get(pk=id)})


def video_stream(request, id):
    return render(request, 'audio_stream.html', {'video_stream': AudioStream.objects.get(pk=id)})


def streaming(request):
    return render(request, 'right.html', {
        'audio_streams': AudioStream.objects.all(),
        'video_stream_sets': VideoStreamSet.objects.all()
    })


def stream_creation(request):
    return render(request, 'stream_creation.html')


def test(request):
    return render(request, 'test.html')


def test_raw(request):
    return render(request, 'test_raw.html')


def test_server(request):
    return render(request, 'test_server.html')
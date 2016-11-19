#coding: utf-8

from django.shortcuts import render
from models import VideoCategory, Video, Author, AudioStream, VideoStream, VideoStreamSet, Article


def index(request):
    return render(request, 'index.html', {'articles' : Article.objects.all()})


def category(request, id):
    return render(request, 'category.html', {'authors': Author.objects.filter(category=id)})


def author(request, id):
    return render(request, 'author.html', {'videos': Video.objects.filter(author=id)})


def article(request, id):
    return render(request, 'article.html', {'article': Article.objects.get(pk=id)})


def audio_stream(request, id):
    return render(request, 'audio_stream.html', {'audio_stream': AudioStream.objects.get(pk=id)})


def video_stream(request, id):
    return render(request, 'audio_stream.html', {'video_stream': AudioStream.objects.get(pk=id)})


def video_storage(request):
    return render(request, 'left.html', {'categories': VideoCategory.objects.filter(pid__isnull=True)})


def streaming(request):
    return render(request, 'right.html', {
        'audio_streams': AudioStream.objects.all(),
        'video_stream_sets': VideoStreamSet.objects.all()
    })


def stream_creation(request):
    return render(request, 'stream_creation.html')

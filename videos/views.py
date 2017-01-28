#coding: utf-8

from django.shortcuts import render
from django.http import JsonResponse
from videos.models import Author, Video, VideoCategory

def category(request, id, url):
    return render(request, 'category.html', {'authors': Author.objects.filter(category=id)})


def author(request, id):
    return render(request, 'author.html', {'videos': Video.objects.filter(author=id)})


def video_storage(request):
    return render(request, 'left.html', {'categories': VideoCategory.objects.filter(pid__isnull=True)})


def default(request):
    videos = [{'src': video.get_url(), 'thumb': video.get_thumb()} for video in Video.objects.all()[:5]]
    return JsonResponse({'thumbnails': videos})

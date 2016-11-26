#coding: utf-8

from django.shortcuts import render
from videos.models import Author, Video, VideoCategory

def category(request, id):
    return render(request, 'category.html', {'authors': Author.objects.filter(category=id)})


def author(request, id):
    return render(request, 'author.html', {'videos': Video.objects.filter(author=id)})


def video_storage(request):
    return render(request, 'left.html', {'categories': VideoCategory.objects.filter(pid__isnull=True)})



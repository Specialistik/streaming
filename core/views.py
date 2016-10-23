from django.shortcuts import render
from models import VideoCategory, Video, Author, AudioStream, VideoStreamSet

def index(request):
    return render(request, 'index.html')
    

def category(request, id):
    return render(request, 'category.html', {'authors': Author.objects.filter(category=id)})
    
    
def author(request, id):
    return render(request, 'author.html', {'videos': Video.objects.filter(author=id)})
    
    
def video_storage(request):
    return render(request, 'left.html', {'categories': VideoCategory.objects.filter(pid__isnull=True)})
    
    
def streaming(request):
    return render(request, 'right.html', {
        'audio_streams': AudioStream.objects.all(),
        'video_stream_sets': VideoStreamSet.objects.all()
    })


def stream_creation(request):
    return render(request, 'stream_creation.html')
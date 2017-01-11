#coding: utf-8

from django.shortcuts import render
from models import Article


def index(request):
    return render(request, 'index.html', {'articles' : Article.objects.all()})



def article(request, id):
    return render(request, 'article.html', {'article': Article.objects.get(pk=id)})


def account(request):
    return render(request, 'account.html')


def profile(request):
    return render(request, 'profile.html')



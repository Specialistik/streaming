#coding: utf-8

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from models import Article, Profile


def index(request):
    return render(request, 'index.html', {'articles' : Article.objects.all()})


def article(request, id):
    return render(request, 'article.html', {'article': Article.objects.get(pk=id)})


def account(request):
    return render(request, 'account.html')


def profile(request):
    return render(request, 'profile.html')


def register(request):
	user = User.objects.create_user(
		request.POST['username'], 
		request.POST['email'], 
		request.POST['password']
	)
	user.save()
	
	#user_profile = user.get_profile()
	#user_profile.phone = request.POST['phone']
	#user_profile.save()
	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	if user is not None:
		login(request, user)
		return JsonResponse({'success': True})
	else:
		return JsonResponse({'success': False, 'message': 'Ошибка авторизации'})

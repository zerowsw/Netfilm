from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

from application.models import *


#web
def index(request):
	return render(request,'index.html')


#movie
def search_movie(request):
	title = request.GET.get("title", "")
	if title:
		qs = list(movie.objects.filter(title__contains=title)[0:11].values())
		return JsonResponse(qs, safe = False)
	else:
		return HttpResponse("false")

def recommend_movie(request):
	# this part for mapreduce
	pass


def get_movie_rate_comment(request):
	title = request.GET.get("title", "")
	# if title:

	pass

def get_movie_info(request):
	pass

#user-basic
def register(request):
	name = request.GET.get("name","")
	email = request.GET.get("email","")
	pw = request.GET.get("pw","")
	if email and pw:
		if(len(pw) < 4):
			return HttpResponse("pwTooShort")
		if(len(user.objects.filter(email=email))):		
			return HttpResponse("email already taken, please login")
		if(len(user.objects.filter(name=name))):			
			return HttpResponse("name already taken, choose another name")
		# from application.models import user
		user.objects.create(name=name, email = email, pw = pw)
		return HttpResponse("success")

def login(request):
	email = request.GET.get('email',"")
	pw = request.GET.get('pw',"")
	if email and pw:
		from application.models import user
		res = user.objects.filter(email = email)
		if res and len(res):
			return HttpResponse("true")
		else:
			return HttpResponse("false")

def change_pw(request):
	email = request.GET.get("email", "")
	old_pw = request.GET.get("old", "")
	new_pw1 = request.GET.get("pw1", "")
	new_pw2 = request.GET.get("pw2", "")
	if email and old_pw:
		if(new_pw1 != new_pw2):
			return HttpResponse("new passwords not match")
		if(user.objects.filter(email=email)[0].pw != old_pw):
			return HttpResponse("old passwords incorrect")
		user.objects.filter(email=email).update(pw=pw)
		return HttpResponse("change password success")
	else:
		return HttpResponse("incorrect input")

def delete(request):
	email = request.GET.get("email","")
	pw = request.GET.get("pw","")
	if email and pw:
		from application.models import user
		user.objects.filter(email = email).delete()
		return HttpResponse("true")

#user-movie
def add_favor(request):    #later
	pass

def get_favor(request):		 #later	
	pass

def get_user_rate_comment(request):
	email = request.GET.get("email", "")
	if email:
		qs = list(movie.objects.filter(title__contains=title)[0:11].values())
		return JsonResponse(qs, safe = False)
	else:
		return HttpResponse("false")	
	pass

def get_user_watched_movies(request):
	pass

def add_watched_movie(request):
	pass



#user-social
def add_friend(request):
	e1 = request.GET.get("email1", "")
	e2 = request.GET.get("email2", "")
	if e1 and e2:
		from application.models import friendship
		friendship.objects.create(email1=e1, email2=e2)
		return HttpResponse("true")
	else:
		return HttpResponse("false")


def get_friend_list(request):
	pass


def deletefriend(request):
	e1 = request.GET.get("email1", "")
	e2 = request.GET.get("email2", "")
	if e1 and e2:
		from application.models import friendship
		friendship.objects.filter(email1=e1, email2=e2).delete()
		return HttpResponse("true")
	else:
		return HttpResponse("false")


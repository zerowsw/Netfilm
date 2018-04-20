from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
# Create your views here.

from application.models import *


#web
def index(request):				#done
	return render(request,'index.html')  

#movie
def search_movie(request):
	title = request.GET.get("title", "")
	if title:
		movies = list(movie.objects.filter(title__contains=title).values())
		if(len(movies)):
			return JsonResponse(movies, safe = False)
		else:
			return HttpResponse("no movies found! Try another keyword")
	else:
		return HttpResponse("false")

def recommend_movie(request):
	# this part for mapreduce
	pass

def get_movie_comment(request):
	title = request.GET.get("title", "")
	if title:
		comments = list(comment.objects.filter(title=title).values())
		if(len(comments)):
			return HttpResponse("no comments yet")	
		return JsonResponse(comments, safe = False)
	else:
		return HttpResponse("false")		
	pass

def get_movie_info(request):
	title =  request.GET.get("title", "")
	if title:
		res = list(movie.objects.filter(title=title)[0].values())
		if res:
			return JsonResponse(res, safe = False)
		else:
			return HttpResponse("nothing found")
	else:
		return HttpResponse("invalid input")
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
		# userid = user.objects.all()
		user.objects.create(name=name, email = email, pw = pw) #,userid=userid?????????????????
		return HttpResponse("success, Userid is")

def login(request):
	email = request.GET.get('email',"")
	pw = request.GET.get('pw',"")
	if email and pw:
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
# def add_favor(request):    #later
# 	pass

# def get_favor(request):		 #later	
# 	pass

def get_user_comment(request):
	name = request.GET.get("name", "")
	if name:
		comments = list(comment.objects.filter(name=name).values())
		# rate = list(comment.objects.filter(email=email)[0:11].values())
		if len(comments):
			return JsonResponse(comments, safe = False)
		else:
			return HttpResponse("no comments yet")	
	else:
		return HttpResponse("invalid input")	

def commnet(request):
	name = request.GET.get("name", "")
	title = request.GET.get("title", "")
	content = request.GET.get("content", "")
	timestamp = request.GET.get("timestamp", "")
	if name and title and content and timestamp:
		comment.objects.create(name =name,title = title, content = content,timestamp = timestamp)
		return HttpResponse("success")	
	else:
		return HttpResponse("error")	
# def get_user_watched_movies(request):  #later
# 	pass

# def add_watched_movie(request):  #later
# 	pass



#user-social
def add_friend(request):
	name1 = request.GET.get("name1", "")
	name2 = request.GET.get("name2", "")
	if name1 and name2:
		friendship.objects.create(name1=name1, name2=name2)
		return HttpResponse("true")
	else:
		return HttpResponse("false")


def get_friend_list(request):
	name = request.GET.get("name", "")
	if name:
		friends=list(friendship.objects.filter(name1=name).values())
		if(len(friends)):
			return JsonResponse(friends, safe = False)
		else:
			return HttpResponse("you have no friends!")


def deletefriend(request):
	name1 = request.GET.get("name1", "")
	name2 = request.GET.get("name2", "")
	if name1 and name2:
		friendship.objects.filter(name1=name1, name2=name2).delete()
		return HttpResponse("true")
	else:
		return HttpResponse("false")


def search_user(request):
	target = request.GET.get("target", "")
	if target:
		search_email = list(friendship.objects.filter(email__contains=target).values())
		search_name = list(friendship.objects.filter(nsme__contains=target).values())
		all_results = search_name + search_email
		if(len(all_results)):
			return JsonResponse(all_results, safe = False)
		else:
			return HttpResponse("no search results")
	else:
		return HttpResponse("invalid input")
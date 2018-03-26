from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
# Create your views here.


def searchmovie(request):
	title = request.GET.get("title", "")
	if title:
		from application.models import movie
		qs = list(movie.objects.filter(title_contains=title).values())
		return JsonResponse(data, safe = False)
	else:
		return HttpResponse("false")


def addfriend(request):
	e1 = request.GET.get("email1", "")
	e2 = request.GET.get("email2", "")
	if e1 and e2:
		from application.models import friendship
		friendship.objects.create(email1=e1, email2=e2)
		return HttpResponse("true")
	else:
		return HttpResponse("false")


def searchfriend(request):
	# email = 
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

def changepw(request):
	email = request.GET.get("email", "")
	pw = request.GET.get("pw", "")
	if email and pw:
		from application.models import user
		user.objects.filter(email=email).update(pw=pw)
		return HttpResponse("true")
	else:
		return HttpResponse("false")

def delete(request):
	email = request.GET.get("email","")
	pw = request.GET.get("pw","")
	if email and pw:
		from application.models import user
		user.objects.filter(email = email).delete()
		return HttpResponse("true")

def register(request):
	email = request.GET.get("email","")
	pw = request.GET.get("pw","")
	if email and pw:
		if(len(pw) < 4):
			return HttpResponse("pwTooShort")
		from application.models import user
		user.objects.create(email = email, pw = pw)
		return HttpResponse("true")

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


def index(request):
	return render(request,'index.html')
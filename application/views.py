from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def searchmovie():
	pass

def addfriend():
	pass

def deletefriend():
	pass

def changepw(request):
	pass

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

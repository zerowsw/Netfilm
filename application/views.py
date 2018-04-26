from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from django.http import HttpResponseRedirect
from application.models import *
from dwebsocket.decorators import accept_websocket
from django.utils import timezone
import json

#web
def index(request):				#done
	try:
		current_name = request.session['login_name']
	except KeyError:
		return render(request,'index.html')
	else:
		return render(request,'index.html',context={'current_name' : current_name})
		

#chat page
def chat(request):
	return render(request,'chat.html', {'username' : request.session.get('username', 'Hongting')})


clients = []
@accept_websocket
def echo(request):
    if request.is_websocket:
        try:
            clients.append(request.websocket)
            for message in request.websocket:
                print(message)
                me=eval(message)#将字符串类型的消息转换为字典型
                print(type(me))
                print(me["name"])
                if not message:
                    break
                for client in clients:
                    print(client)
                    client.send(message)
        finally:
            clients.remove(request.websocket)


def loginpage(request):

	return render(request,'loginpage.html')

def registerpage(request):
	return render(request,'registerpage.html')

def searchpage(request):
	name = request.session['user_name']
	return render(request, 'searchpage.html',context={'name':name})
	# if request.method == 'POST':
	# 	return render(request, 'searchpage.html')
	# else:
	# 	return render(request,'searchpage.html')

def movieinfo(request):
	return render(request,'movie-info.html')

def userprofile(request):
	return render(request,'userprofile.html')

def recommendpage(request):
	return render(request,'recommend.html')

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

# from django.http import HttpResponse
# from django.template import loader
#
# def searchpage(request):
#     # View code here...
#     t = loader.get_template('./templates/searchpage.html')
#     c = {'foo': 'bar'}
#     return HttpResponse(t.render(c, request), content_type='application/xhtml+xml')
#

def recommend_movie(request):
	# this part for mapreduce
	user_name = request.GET.get("name", "")

	import random as rd
	all_movie = list(movie.objects.all().values())
	sample_size = 1000
	threshold = 8.0
	sample_movie = rd.sample(all_movie,sample_size)
	good_sample_movie = [sample_movie[i] for i in range(0,sample_size) if sample_movie[i]['vote_average']>threshold]
	if(len(good_sample_movie)):
		return JsonResponse(good_sample_movie, safe = False)
	else:
		return HttpResponse("no recommendations yet!")



def get_movie_comment(request):
	title = request.GET.get("title", "")
	if title:
		comments = list(comment.objects.filter(title=title).values())
		if(len(comments)):
			return JsonResponse(comments, safe = False)
		else:
			return HttpResponse("no comments yet")
	else:
		return HttpResponse("false")		
	pass

def get_movie_info(request):
	title =  request.GET.get("title", "")
	if title:
		res = list(movie.objects.filter(title=title)[0:1].values())
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
		# if(len(pw) < 4):
		# 	return HttpResponse("pwTooShort")
		if(len(user.objects.filter(email=email))):		
			return HttpResponse("email already taken, please login")
		if(len(user.objects.filter(name=name))):			
			return HttpResponse("name already taken, choose another name")
		# userid = user.objects.all()

		all_users = user.objects.all()
		user_id_set = [all_users[i].user_id for i in range(0,len(all_users))]
		new_id = max(user_id_set) + 1

			# user.objects.create(user_id = new_id,name=name, email = email, pw = pw) #,userid=userid?????????????????
			# u = user(user_id = new_id,name=name, email = email, pw = pw)
			# u.save()
		user.objects.get_or_create(user_id = new_id,name=name, email = email, pw = pw)
		return HttpResponse("success, newid  is %d"%(new_id))
		# return HttpResponse("success, Userid is",user.objects.filter(name=name)[0].user_id)
		# return HttpResponse("success, Userid is",100)

def login(request):
	if request.method == 'POST':
		email = request.GET.get('email',"")
		pw = request.GET.get('pw',"")
		request.session['username'] = email
		request.session['is_login'] = True
		#return HttpResponseRedirect('/searchpage/')
		# if email and pw:
		# 	res = user.objects.filter(email = email,pw = pw)
		# 	if res and len(res):
		# 		name = res[0].name
		# 		request.session['username'] = name
		# 		request.session['is_login'] = True
		# 		# return HttpResponse("You have successfully logged in! ")
        #
		# 		return HttpResponseRedirect('/searchpage/')
		# 		# return HttpResponse(name)
		# 	else:
		# 		return HttpResponse("Can't log in, please check your account or password!")
	return render(request,'loginpage.html')

def logout(request):
	name = request.GET.get('name',"")
	try:
		del request.session['login_name']
	except KeyError:
		pass
	else:
		return HttpResponse("You're logged out.")


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

def make_comment(request):
	name = request.GET.get("name", "")
	title = request.GET.get("title", "")
	content = request.GET.get("content", "")
	timestamp = request.GET.get("timestamp", "")
	if name and title and content and timestamp:
		comment.objects.create(name =name,title = title, content = content,timestamp = timestamp)
		return HttpResponse("successful comment!")	
	else:
		return HttpResponse("invalid input")	

#user-social
def add_friend(request):
	name1 = request.GET.get("name1", "")
	name2 = request.GET.get("name2", "")
	if name1 and name2:
		friendship.objects.create(name1=name1, name2=name2)
		return HttpResponse("Added!")
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
		return HttpResponse("Deleted!")
	else:
		return HttpResponse("false")


def search_user(request):
	target = request.GET.get("target", "")
	if target:
		search_email = list(user.objects.filter(email__contains=target).values())
		if(len(search_email)):
			return JsonResponse(search_email, safe = False)
		search_name = list(user.objects.filter(name__contains=target).values())
		if(len(search_name)):
			return JsonResponse(search_name, safe = False)
		else:
			return HttpResponse("no search results")
	else:
		return HttpResponse("invalid input")



from django.shortcuts import render

# Create your views here.
def register(request):
	email = request.GET.get("email","")
	pw = request.GET.get("pw","")
	if email and pw:
		if(len(pw) < 4):
			return HttpResponse("pwTooShort")
		from testapp.models import user
		user.objects.create(email = email, pw = pw)
		return HttpResponse("true")

def login(request):
    email = request.GET.get('email',"")
    pw = request.GET.get('pw',"")
    if email and pw:
    	from testapp.models import user
    	res = user.objects.filter(email = email)
    	if res and len(res):
    		return HttpResponse("true")
    	else:
    		return HttpResponse("false")


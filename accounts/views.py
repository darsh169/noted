from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.urls import reverse
from accounts.models import Notes
import accounts

# from django.views.decorators.csrf import ensure_csrf_cookie

# @ensure_csrf_cookie
# @csrf_protect

# import json

# Create your views here.
def Home(request):
	# return HttpResponse("Hello wolrd")
	return render(request,"login4.html")

def Regester(request):
	return render(request,"register.html")


# class UsernameValid(View):
# 	def post(self,request):
# 		data=jason.loads(request.body)#converts json data to python readable dict
# 		username=data['username']



def DoRegister(request):
	if request.method=="POST":
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']
		msgs=[]
		if(password1==password2):
			if User.objects.filter(username=username).exists():
				msgs.append("Username already taken")

			elif User.objects.filter(email=email).exists():
				msgs.append("email already taken")

			else:
				user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
				user.save()
				msgs.append(username+" Successfuly Registered !")
			return render(request,"login4.html",{'msgs':msgs})
		msgs.append("Password didnt match")
		return render(request,"register.html",{'msgs':msgs})


def Login(request):
	return render(request,"login.html")

def Account(request):
	# if request.method=='POST':
	id=request.session['id']
	user=User.objects.get(id=id)
	notes=Notes.objects.all().filter(user_id=user.id)
	try:
		note_id=request.GET['note_id']
		note=Notes.objects.get(id=note_id)
		# return HttpResponseRedirect('account')
	except:
		note=None
	
	return render(request,"accounts.html",{'User':user,'notes':notes,'note':note})

def DoLogin(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']

		user=auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			request.session['id']=user.id
			return HttpResponseRedirect(reverse(Account))#if we use render here then csrf error wll show up as rendering again will not recognize csrf token
			# # email=user.email
			# return redirect("/account")
		msgs=[]
		msgs.append("Invalid User")
		return render(request,"login4.html",{'msgs':msgs})

def DoLogout(request):
	auth.logout(request)
	return redirect('/')

def SaveNote(request,user_id):
	title=request.POST['title']
	content=request.POST['content']
	user=User.objects.get(id=user_id)
	Notes(title=title,content=content,user_id=user).save()
	return HttpResponseRedirect(reverse(Account))# in reverse we can pass the function

def ShowNote(request):
	note_id=request.GET['note_id']
	note=Notes.objects.get(id=note_id)
	# notes=request.session['notes']
	return render(request,"notes.html",{'note1':note})
	
def Delete(request,note_id):
	note=Notes.objects.filter(id=note_id).delete()
	return HttpResponseRedirect('/account')

def Update(request,note_id):
	title=request.POST['title']
	content=request.POST['content']
	Notes.objects.filter(id=note_id).update(title=title,content=content)
	return HttpResponseRedirect('/account?note_id=note_id')

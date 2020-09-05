from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from .forms import User_RegistrationForm


def signup(request):
    if request.method == 'POST':
    	username = request.POST['email_id']
    	password = request.POST['password']
		try:
			record = User_registration.objects.get(email_id=username, password=password)
			#print(record)
			if record is not None:
				return HttpResponse('thanks for registeration')
				#return redirect('/logsuccess')
			else:
				return HttpResponse('Invalid')
		except:
			return HttpResponse('invalid')
	else:
		frm = User_RegistrationForm()
	return render(request,'registration/login.html',{'stu':frm})

		

def login(request):
	if request.method == 'POST':
		username = request.POST['email']
		password = request.POST['passwd']
		try :
		#user = auth.authenticate(userid=username,passwd=password)
			record = User_registration.objects.get(email=username,passwd=password)

			#print(record)
			if record is not None :
				return HttpResponse('thanks for register')
				#return redirect('/logsuccess')
			else:
				return HttpResponse('Invalid')
		except:
			return HttpResponse('invalid')
	else:
		frm = User_RegistrationForm()
	return render(request,'login.html',{'stu':frm})



def home(request):
	return render(request, 'home.html', {})
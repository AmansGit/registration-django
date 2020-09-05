from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from .forms import User_RegistrationForm


# def signup(request):
#     if request.method == 'POST':
#         form = User_RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = User_RegistrationForm()
#     return render(request, 'signup.html', {'form': form})



def home(request):
	return render(request, 'home.html', {})
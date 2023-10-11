from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.forms import  CustomUserForm
from django.contrib import messages
from django.contrib.auth import  authenticate, login, logout


# Create your views here.

def home(request):
    return render(request, 'index.html')

def signuppage(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully! Login to Continue")
            return redirect('loginpage')
    context = {'form':form}
    return render(request, 'register.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect('/')
    else:
        if request.method == "POST":
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            
            user = authenticate(request,username=name,password=passwd)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect('/')
            else:
                    messages.error(request, "Invalid Username or Password")
                    return redirect('loginpage')
        return render(request, 'signin.html')
    
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logout Successfully")
    return redirect('/')
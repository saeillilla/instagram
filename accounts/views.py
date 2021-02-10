from django.shortcuts import render,redirect
from .forms import Create_New_user
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form1 = Create_New_user(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/accounts/login/')
        else:
            return render(request,'accounts/login.html',{'form':form1})
        pass
    else:
        form1 = Create_New_user()
        return render(request,'accounts/login.html',{'form':form1})

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        print(user)
        if user:
            login(request,user)
            return redirect('/posts/home/')
        else:
            return render(request,'accounts/sign_in.html',{'error':True })


    else:

        return render(request,'accounts/sign_in.html')
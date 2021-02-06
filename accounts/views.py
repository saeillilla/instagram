from django.shortcuts import render,redirect
from .forms import Create_New_user

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form1 = Create_New_user(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/')
        else:
            return render(request,'accounts/login.html',{'form':form1})
        pass
    form1 = Create_New_user()
    return render(request,'accounts/login.html',{'form':form1})

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    else:

        return render(request,'accounts/sign_in.html')
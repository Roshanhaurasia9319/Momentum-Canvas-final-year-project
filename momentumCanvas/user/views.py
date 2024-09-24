from django.shortcuts import render, HttpResponse, redirect
from .models import UserData


# Create your views here.
def index(request):
    try:
          if request.method=='POST':
            name=request.POST.get('name')
            username=request.POST.get('username')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            leetcode=request.POST.get('leetcode')
            codechef=request.POST.get('codechef')
            geekforgeeks=request.POST.get('geekforgeeks')
            github=request.POST.get('github')
            newUser=UserData(name=name, username=username, email=email, phone=phone, 
                             leetcode=leetcode, codechef=codechef, geekforgeeks=geekforgeeks, github=github)
            newUser.save()
            return redirect(dashboard)
            
    except:
        return HttpResponse("ERROR")
  
    return render(request, 'user/index.html')

def dashboard(request):
    return render(request, "user/dashboard.html")
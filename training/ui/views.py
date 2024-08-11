from django.shortcuts import render,HttpResponse
from ui.models import Login

def show(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
 
        namaste = Login(username=username, password=password)
        namaste.save()
        return HttpResponse("Success")
        
    
    return render(request, "login.html")

from django.shortcuts import render

# Create your views here.


def UserLogin(request): 
    return render(request, 'LoginApp/login.html')



def Register(request): 
    return render(request, 'LoginApp/register.html')
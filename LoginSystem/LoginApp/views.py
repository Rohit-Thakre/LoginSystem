from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm

from django.contrib.auth import login, logout , authenticate

from django.contrib.auth.models import User
# Create your views here.


def UserLogin(request): 
    form = LoginForm()

    if request.method == 'POST': 
        username  = request.POST.get('username')
        password  = request.POST.get('password')
        print(username)

        try: 
            in_db = User.objects.get(username = username)  
            
            if in_db is not None:   
                check = authenticate(username = username, password= password)


                if check: 
                    login(request, check)
                    return HttpResponse('successfully loged in')
                else: 
                    return HttpResponse('Password Incorrect')

        except:
            return HttpResponse("User name doesn't exists")



    return render(request, 'LoginApp/login.html', {'form': form})



def Register(request): 
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid: 
            instance = form.save(commit= False)
            instance.username = request.POST.get('first_name') + request.POST.get('last_name')

            instance.save()
            login(request, instance)

            
            return HttpResponse("acount created and logged in.")


    return render(request, 'LoginApp/register.html', {'form': form})




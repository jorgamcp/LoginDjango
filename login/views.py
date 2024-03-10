from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout as django_logout,authenticate as django_authenticate
from django.contrib.auth import  login as django_login

from django.urls import reverse
# Create your views here.
def index(request):
    form = {
        'data':AuthenticationForm()
    }
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        print("A que quieres iniciar sesion")
        print(f"username es {username} y password es {password}")
        
        user = django_authenticate(request,username=username,password=password)
        if user is not None:
            print("Bienvenido " + user.get_username() )
            django_login(request,user)
            return redirect('protegido')
        else:
            print(user)

    

    return render(request,'index.html',context={'form':form})

def logout(request):
    django_logout(request)
    return redirect("/",permanent=True)


@login_required(login_url="/")
def protegido(request,data=None):


    return render(request,'secret.html')

@login_required(login_url='/')
@user_passes_test(lambda u: u.is_superuser,login_url='/protegido')
def administradores(request):
    if user_passes_test(lambda u: u.is_superuser):
        data = {'data':'eres UN admin'}
    else:
        data = {'data':'no tienes permiso para ver esta pagina porque no eres administrador/a'}
        return render(request,'secret.html',data)
    return render(request,'admin.html',data)
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

from CoinControllapp.forms import LoginForm, UserRegistrationForm
# Create your views here.




def home(request):
    return render(request, 'home.html')

#LOGIN FUNCIONALIDAD
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            #en caso de que haya un usuario con ese nombre y contraseña lo retornara 
            if user is not None:
                if user.is_active:
                    #comprueba que el usuario logueado este acitvo , lo maneja Django Automaticamente 
                    login(request, user)
                    return redirect('home')
                else:
                    return render(request, 'login.html', {'error': 'Usuario no activo.'})
            else:
                return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})





def register(request):
    error = ''  
    if request.method== 'POST':
        user_form= UserRegistrationForm(request.POST)
        if user_form.is_valid():
            
            try:
                new_user = user_form.save(commit=False) # de momento sera falso para que securicemos la contraseña
                new_user.set_password(
                user_form.cleaned_data['password']
                )# set_password encripta  la contraseña que se le pasa desde cleaned data => que recoge ya los datos validados 
               
                new_user.save()
                login(request,new_user)
                return redirect('home')
            except IntegrityError:
                error ='An exception occurred'
                print(error)
                return render(request, 'register.html',{'user_form':user_form,'error': error})
        else:
            #me devuelve los errores del metodo ya creado en forms.py
            error = user_form.errors.as_data()
            return render(request, 'register.html',{'user_form':user_form,'error': error})
    else: 
        user_form= UserRegistrationForm()
        return render(request, 'register.html',{'user_form':user_form,'error': error})
    
    
    
    
    
    
    
    
    
    


def logout_view(request):
    logout(request)
    return render(request,'home.html')


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.utils import timezone
import datetime
from django.utils.timezone import utc

from .filters import VooFilter

from .models import *
from .forms import *

from .decorators import unauthenticated_user, allowed_users, admin_only


now = datetime.datetime.now()

# Home page

def home(request):
    return render(request, 'sistema/home.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'sistema/login.html', {'form':AuthenticationForm()} )
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            # Se o usuario nao existir
            return render(request, 'sistema/login.html', {'form':AuthenticationForm(), 'error':'Usuário ou senha inválido.'} )
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required(login_url='login')
@admin_only
def gestaousuarios(request):
    List = Passageiro.objects.all()
    return render(request, 'sistema/gestaousuarios.html', {'List': List})

@login_required(login_url='login')
@admin_only
def aeroporto(request):
    List = Aeroporto.objects.all()
    return render(request, 'sistema/aeroporto.html', {'List': List})


@login_required(login_url='login')
@admin_only
def newuser(request):
    if request.method == 'GET':
        return render(request, 'sistema/newuser.html', {'form':UserCreationForm()} )
    else:
        # Create a new user
        if request.POST['password1'] == request.POST['password2']: # Validacao da confirmacao da senha
            try:
                user = User.objects.create_user(request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
                user.save() # Cria usuario no banco de dados
                group = Group.objects.get(name='cliente')
                user.groups.add(group)
                return redirect('gestaousuarios')

            except IntegrityError:
                # Retorna se o usuario ja existir
                return render(request, 'sistema/newuser.html', {'form':UserCreationForm(), 'error':'O nome de usuário ou e-mail já existe. Por favor escolha outro.'} )
        else:
            return render(request, 'sistema/newuser.html', {'form':UserCreationForm(), 'error':'Senha divergente. Digite novamente'} )

@login_required(login_url='login')
@admin_only
def createpassageiro(request):
    if request.method == 'GET':
        return render(request, 'sistema/createpassageiro.html', {'form':CreatePassageiroForm()} )
    else:
        try:
            form = CreatePassageiroForm(request.POST)
            novo_passageiro = form.save(commit=False)
            novo_passageiro.save() # Salvar no banco de dados

            user = User.objects.create_user(request.POST['email'], email=request.POST['email'])
            user.save() # Cria usuario no banco de dados
            group = Group.objects.get(name='cliente')
            user.groups.add(group)
            return redirect('gestaousuarios')
        except IntegrityError:
            # Retorna se o usuario ja existir
            return render(request, 'sistema/newuser.html', {'form':UserCreationForm(), 'error':'O nome de usuário ou e-mail já existe. Por favor escolha outro.'} )


@login_required(login_url='login')
@admin_only
def monitoramento(request):
	return render(request, 'sistema/monitoramento.html')

@login_required(login_url='login')
@admin_only
def checkin(request):
    List = Check_In.objects.all()
    return render(request, 'sistema/checkin.html', {'List': List})

@login_required(login_url='login')
@admin_only
def novocheckin(request):
    return render(request, 'sistema/novocheckin.html')

@login_required(login_url='login')
@admin_only
def mala(request):
    List = Mala.objects.filter(user=request.user, datecompleted__isnull=True) # Pega todos os objetos Mala do usuario logado
    return render(request, 'sistema/rastrear.html', {'List': List})


@login_required(login_url='login')
def checkincliente(request):
    List = Check_In.objects.all()
    return render(request, 'sistema/checkincliente.html', {'List': List})

@login_required(login_url='login')
def viewmala(request):
    return render(request, 'sistema/viewmala.html')
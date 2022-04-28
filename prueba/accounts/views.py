from email import message
from multiprocessing import context
import re
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group


def registarAdminEmpresa(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='adminEmpresa')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('home')
    context = {'form':form}
    return render(request, 'accounts/registar_adminEmpresa.html', context)


@unauthenticated_user
def registerApp(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='adminEmpresa')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginApp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def home(request):
    empresas = Empresa.objects.all()
    administradores = Administrador.objects.all()
    context = {'empresas':empresas, 'administradores':administradores}
    return render(request, 'accounts/dashboard.html', context)

def userPage(request):
	context = {}
	return render(request, 'accounts/user.html', context)



@login_required(login_url='login')
def empresa(request):
    empresas = Empresa.objects.all()
    return render(request, 'accounts/empresas.html', {'empresas':empresas})

@login_required(login_url='login')
def sede(request):
    return render(request, 'accounts/sedes.html')

@login_required(login_url='login')
def admnistrador(request, pk):
    administradores = Administrador.objects.all()
    administrador = Administrador.objects.get(id=pk)
    users = User.objects.values()
    usernames = User.objects.values_list('username', flat=True)
    context = {'administrador':administrador, 'administradores':administradores, 'usernames':usernames}
    return render(request, 'accounts/administradores.html', context)

def usuarios(request):
    return render(request, 'accounts/usuarios.html')

@login_required(login_url='login')
def crearEmpresa(request):
    form = EmpresaForm()
    if request.method == 'POST':
        #print('Printing POST', request.POST)
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form':form}
    return render(request, 'accounts/empresa_form.html', context)

@login_required(login_url='login')
def actualizarEmpresa(request, pk):
    empresa= Empresa.objects.get(id=pk)
    form = EmpresaForm(instance=empresa)

    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form':form}
    return render(request, 'accounts/empresa_form.html', context)

@login_required(login_url='login')
def eliminarEmpresa(request, pk):
    empresa= Empresa.objects.get(id=pk)
    if request.method == 'POST':
        empresa.delete()
        return redirect('/')
    context = {'item':empresa}
    return render(request, 'accounts/eliminar.html', context)

def crearAdministrador(request):
    form = AdministradorForm()
    if request.method == 'POST':
        #print('Printing POST', request.POST)
        form = AdministradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form':form}
    return render(request, 'accounts/administrador_form.html', context)

def eliminarAdministrador(request, pk):
    administrador = Administrador.objects.get(id=pk)
    if request.method == 'POST':
        administrador.delete()
        return redirect('/')
    context = {'item':administrador}
    return render(request, 'accounts/eliminar_admin.html', context)

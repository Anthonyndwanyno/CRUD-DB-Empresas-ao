from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, addEmpresaForm
from .models import Empresa

# Create your views here.
def home(request): 
    empresas= Empresa.objects.all()

    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(request, username= username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login feito com sucesso")
            return redirect('home')
        else:
            messages.success(request, "Ocorreu algum errro, tenta novamente  ")
            return redirect('home')
    else:
        return render(request, "home.html",{'empresas':empresas})
 
def user_logout(resquest):
    logout(resquest)
    messages.success(resquest,"Saiu com sucesso")
    return redirect('home')

def user_register(request):
    if request.method== 'POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login user
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user= authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Feito com sucesso")
            return redirect('home')
    else:
        form= SignUpForm()
        return render(request, "register.html",{'form':form})
    return render(request, "register.html",{'form':form})

def empresa_record(request, pk):
    if request.user.is_authenticated:
        empresa_record= Empresa.objects.get(nif=pk)
        return render(request, "empresa_record.html",{'empresa_record':empresa_record})
    else:
        messages.success(request, "Precisa fazer o Login Para visualizar")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it= Empresa.objects.get(nif=pk)
        delete_it.delete()
        messages.success(request, "Foi apagado com sucesso")
        return redirect('home')
    else:
        messages.success(request, "Precisa fazer o Login Para realizar esta acção")
        return redirect('home')

def add_record(request):
    form= addEmpresaForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record= form.save()
                messages.success(request, "Registado com sucesso")
                return redirect('home')
        return render(request, "add_record.html", {'form': form})
    else:
        messages.success(request, "Falha ao Registar")
        return redirect('home') 
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record= Empresa.objects.get(nif=pk)
        form= addEmpresaForm(request.POST or None, instance= current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Atualizado com sucesso")
            return redirect('home')
        return render(request, "update_record.html", {'form': form})
    else:
        messages.success(request, "Precisa faszer o login")
        return redirect('home')
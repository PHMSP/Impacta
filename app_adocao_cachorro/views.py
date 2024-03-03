from django.shortcuts import render, redirect
from .models import Doador  # Importe o modelo Doador
from django.contrib import messages

def home(request):
    return render(request, 'adocao/home.html')

def cadastro_doador(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        
        # Salvar os dados do doador no banco de dados
        doador = Doador(nome=nome, email=email, telefone=telefone)
        doador.save()
        
        # Redirecionar o usuário de volta para a página inicial
        return redirect('home')
    else:
        return render(request, 'adocao/cadastro_doador.html')

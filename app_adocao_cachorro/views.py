from django.shortcuts import render, redirect
from .models import Doador  # Importe o modelo Doador
from .models import Cachorro # Importe o modelo Cachorro
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

def cadastro_cachorro(request):
    if request.method == 'POST':
        # Extrair os dados do POST
        idade = request.POST['idade']
        estado = request.POST['estado']
        cidade = request.POST['cidade']
        raca = request.POST['raca']
        genero = request.POST['genero']
        descricao = request.POST['descricao']
        email_doador = request.POST['email_doador']  # Aqui usamos o email do doador

        # Verificar se o doador com o email fornecido existe
        try:
            doador = Doador.objects.get(email=email_doador)
        except Doador.DoesNotExist:
            return render(request, 'adocao/cadastro_cachorro.html', {'error_message': 'Doador não encontrado'})

        # Salvar os dados do cachorro no banco de dados
        cachorro = Cachorro.objects.create(idade=idade, estado=estado, cidade=cidade, raca=raca, genero=genero, descricao=descricao, doador=doador)
        
        # Redirecionar o usuário de volta para a página inicial
        return redirect('home')
    else:
        return render(request, 'adocao/cadastro_cachorro.html')
import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Doador, Cachorro
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

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

def lista_cachorro(request):
    estado = request.GET.get('estado')
    cidade = request.GET.get('cidade')

    if estado and cidade:
        cachorros = Cachorro.objects.filter(estado=estado, cidade=cidade)
    else:
        cachorros = Cachorro.objects.all()

    # Buscar URLs das imagens dos cachorros na API The Dog API
    for cachorro in cachorros:
        cachorro.imagem_url = get_imagem_url()

    return render(request, 'adocao/lista_cachorro.html', {'cachorros': cachorros, 'estado': estado, 'cidade': cidade})

def get_imagem_url():
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "live_vRgCbdWFDsEV5ZC1MpHXYn9iaRJLy7zbDXac5hARGvICeIdt5tQKokFkgOT8WAXx"
    }
    response = requests.get("https://api.thedogapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1", headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data and 'url' in data[0]:
            return data[0]['url']
    return None

def deletar_cachorro(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        try:
            doador = Doador.objects.get(email=email, telefone=telefone)
            cachorros = Cachorro.objects.filter(doador=doador)
            if 'cachorro_id' in request.POST:
                cachorro_id = request.POST.get('cachorro_id')
                # Verificar se o cachorro com o ID fornecido pertence ao doador
                cachorro = cachorros.filter(id=cachorro_id).first()
                if cachorro:
                    cachorro.delete()
                    messages.success(request, 'Cachorro deletado com sucesso.')
                    return redirect('home')
                else:
                    error_message = 'Cachorro não encontrado ou não pertence a este doador.'
                    return render(request, 'adocao/deletar_cachorro.html', {'error_message': error_message})
            return render(request, 'adocao/deletar_cachorro.html', {'cachorros': cachorros, 'doador': doador})
        except Doador.DoesNotExist:
            error_message = 'Doador não encontrado. Verifique o e-mail e telefone fornecidos.'
            return render(request, 'adocao/deletar_cachorro.html', {'error_message': error_message})

    return render(request, 'adocao/deletar_cachorro.html')
from django.shortcuts import render


# Create your views here.

def retornar_index(request):
    nome = 'Karen'
    sobrenome = 'Elisa'
    contexto = {
        'nome':nome,
        'sobrenome': sobrenome
    }
    return render(request, 'index.html', contexto)



    def sobre(request):
        salada_de_frutas = ['maçã', 'Uva']
        nome = 'Karen'
    if nome == 'Karen'
       status = 'OI'
       
    elif nome:
        status = 'Preenchido'
    else:
        status = 'Inválido'

    contexto = {
        'salada_de_frutas': salada_de_frutas
        'nome': nome.lower(),
        'status': status
    }
        

    return render(request, 'sobre.html', contexto)
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

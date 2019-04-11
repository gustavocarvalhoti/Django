from django.shortcuts import render

'''
Ao digitar http://localhost:8000/ ele chama essa pagina e retorna o index.html
'''


def index(request):
    return render(request, 'index.html')


def exibir(request, perfil_id):
    print 'ID do perfil recebido -> %s ' % (perfil_id)
    return render(request, 'perfil.html')

from django.shortcuts import render
from perfis.models import Perfil

'''
Ao digitar http://localhost:8000/ ele chama essa pagina e retorna o index.html
'''


def index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all()})


def exibir(request, perfil_id):
    # print 'ID do perfil recebido -> %s ' % (perfil_id)
    # perfil = Perfil()
    perfil = Perfil.objects.get(id=perfil_id)

    # if perfil_id == '1':
    # perfil = Perfil('Gustavo', 'gu@terra.com', '3838-5638', 'Padtec')

    return render(request, 'perfil.html', {"perfil": perfil})

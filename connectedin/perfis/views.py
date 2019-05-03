from perfis.models import Perfil, Convite
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

'''
Ao digitar http://localhost:8000/ ele chama essa pagina e retorna o index.html
'''


# Decorator
# @permission_required('perfis.add_convite', raise_exception=True)
@login_required
def index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all(), 'perfil_logado': get_perfil_logado(request)})


@login_required
def exibir(request, perfil_id):
    # print 'ID do perfil recebido -> %s ' % (perfil_id)
    # perfil = Perfil()
    perfil = Perfil.objects.get(id=perfil_id)

    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()

    # if perfil_id == '1':
    # perfil = Perfil('Gustavo', 'gu@terra.com', '3838-5638', 'Padtec')
    return render(
        request, 'perfil.html',
        {
            "perfil": perfil,
            "ja_eh_contato": ja_eh_contato,
            'perfil_logado': get_perfil_logado(request)
        }
    )


@login_required
def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')


@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')


@login_required
def get_perfil_logado(request):
    return request.user.perfil
    # return Perfil.objects.get(id=1)

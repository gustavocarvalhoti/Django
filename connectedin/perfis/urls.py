from django.conf.urls import patterns, include, url
from perfis import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.exibir, name='exibir'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar'),
)

'''
url(r'^$', 'perfis.views.index')            <- http://localhost:8000/
url(r'^perfis$', 'perfis.views.exibir')     <- http://localhost:8000/perfis
url(r'^perfis/\d+$', 'perfis.views.exibir') <- http://localhost:8000/perfis/12 (1 ou + digitos)
url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.exibir') <- Espera o perfil_id

OlD - url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.exibir', name='exibir'),
NEW - 
'''
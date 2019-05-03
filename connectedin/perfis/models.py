from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    # email = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15, null=False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('self')  # Auto relacionamento com ele mesmo
    usuario = models.OneToOneField(User, related_name="perfil")

    # Se comporta como se fosse atrinuto
    @property
    def email(self):
        return self.usuario.email

    def convidar(self, perfil_convidado):
        print 'Solicitante -> %s %s' % (self.id, self.nome)
        print 'Convidado   -> %s %s' % (perfil_convidado.id, perfil_convidado.nome)
        convite = Convite(solicitante=self, convidado=perfil_convidado)
        # convite = Convite(solicitante=perfil_convidado, convidado=self)
        convite.save()


class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, related_name='convites_recebidos')

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)  # Add
        self.solicitante.contatos.add(self.convidado)  # Add
        self.delete()  # Deleta o convite

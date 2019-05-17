from django.db import models

# Create your models here.
class Reacao(models.Model): 
    TIPOS_REACOES = (('c', 'curtir'),('a', 'amar'),('r', 'rir'), ('i', 'impressionar'),
    ('t', 'triste'), ('grr', 'irritar'))
    tipo = models.CharField(max_length=1, choices=TIPOS_REACOES)
    data = models.DateTimeField()


class Usuario(models.Model):
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=30)
    data_de_nascimento = models.DateField("Nascimento")

class Perfil(models.Model):
    nome = models.CharField(max_length=254)
    usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE, related_name="perfis")
    contatos = models.ManyToManyField("self")

class Postagem(models.Model):
    texto = models.CharField(max_length=254)
    data = models.DateTimeField()
    reacoes = models.ManyToManyField(Reacao)

class Timeline(models.Model):
    postagens = models.ManyToManyField(Postagem)


class Comentario(models.Model):
    texto = models.CharField(max_length=254)
    data = models.DateTimeField()
    perfil = models.ForeignKey(Perfil,models.CASCADE)


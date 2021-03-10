from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save


class info_cliente(models.Model):
    nome = models.CharField(max_length=50, null=False)
    descricao = models.CharField(max_length = 200, blank=True, null=True)
    #Tags = models.ManyToManyField(tags)
    #Lembre = models.ManyToManyField(lembretes)
    ativo = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome

class tags(models.Model):
    Info_Cliente = models.ForeignKey(info_cliente, on_delete = models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class lembretes(models.Model):
    OP = (
        ("S", "Sim"),
        ("N", "Não"),
    )
    Info_Cliente = models.ForeignKey(info_cliente, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    concluido = models.CharField(max_length=3, choices=OP, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #cliente_id = models.ManyToManyField(cliente)

    def __str__(self):
        return self.descricao




class status(models.Model):

    OP = (

        ('S', 'Sim'),
        ('N', 'Não'),
)
    Info_Cliente = models.ForeignKey(info_cliente, on_delete=models.CASCADE)
    descricao = models.TextField(null=True, blank=True)
    data_hora = models.DateTimeField(auto_now_add=True)
    concluido = models.CharField(max_length=3, choices=OP)
    ativo = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao



class centro_custos(models.Model):
    OP = (
        ("S", "Sim"),
        ("N", "Não"),
    )

    #cliente_id = models.ForeignKey(cliente, on_delete=models.CASCADE)
    Info_Cliente = models.ForeignKey(info_cliente, on_delete = models.CASCADE)
    descricao = models.TextField()
    venda_concluida = models.CharField(max_length=3, choices=OP, blank=True, null=True)
    valor = models.IntegerField(blank=True, null=True)
    custo_do_produto = models.IntegerField(blank=True, null=True)
    custo_do_frete = models.IntegerField(blank=True, null=True)
    comissao = models.IntegerField(blank=True, null=True)
    ativo = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao


class cliente(models.Model):
    #nome = models.CharField(max_length=50, blank=True, null=True)
    info = models.ForeignKey(info_cliente, on_delete = models.CASCADE)
    Tags = models.ManyToManyField(tags)
    Status = models.ForeignKey(status, on_delete = models.CASCADE)
    Lembre = models.ManyToManyField(lembretes)
    C_custos = models.ForeignKey(centro_custos, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome

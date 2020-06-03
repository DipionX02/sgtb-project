from django.db import models
from django.contrib.auth.models import User


class Passageiro(models.Model):
    nome  = models.CharField(max_length=250)
    cpf   = models.CharField(max_length=14)
    email = models.EmailField(max_length = 254)
    data_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome

class Mala(models.Model):
    data = models.DateField()
    rfid = models.CharField(max_length=12)
    passageiro = models.ForeignKey(Passageiro, on_delete=models.CASCADE)
    def __str__(self):
        return self.rfid

class Estado(models.Model):
    uf  =  models.CharField(max_length=2)
    def __str__(self):
        return self.uf

class Cidade(models.Model):
    nome  =  models.CharField(max_length=250)
    uf = models.ForeignKey(Estado,on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Aeroporto(models.Model):
    nome    = models.CharField(max_length=250)
    cidade  = models.ForeignKey(Cidade,on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Check_In(models.Model):
    passageiro = models.ForeignKey(Passageiro, on_delete=models.CASCADE)
    aeroporto = models.ForeignKey(Aeroporto, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.passageiro.nome


'''
class Voo(models.Model):
    origem = models.OneToOneField(Aeroporto, on_delete=models.CASCADE, primary_key=True)
    destino = models.CharField(max_length=14)
    data = models.DateField()

class Check_In(models.Model):
    passageiro = models.ForeignKey(Passageiro, on_delete=models.CASCADE)
    voo = models.ForeignKey(Voo, on_delete= models.SET_NULL, null=False)






def __str__(self):
    characters = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for x in range(16):
        codigo += random.choice(characters)
    return codigo_rastreio = codigo


class Estado(models.Model):
    uf  =  models.CharField(max_length=2)

class Cidade(models.Model):
    nome  =  models.CharField(max_length=250)
    uf = models.ForeignKey('Estado')

class Aeroporto(models.Model):
    nome    = models.CharField(max_length=250)
    cidade  = models.ForeignKey('Cidade')

class Voo(models.Model):
    origem = models.ForeignKey('Aeroporto')
    destino = models.ForeignKey('Aeroporto')
    data = models.DateField()

class Check_In(models.Model):
    passageiro = models.ForeignKey(Passageiro)
    voo = models.ForeignKey('Voo', on_delete= models.SET_NULL)

'''
from django.db import models

# Create your models here.

class SectorActividade(models.Model):
    id_sector = models.AutoField(primary_key=True)
    nome_sector = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_sector

class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=100)
    cidade = models.CharField(max_length=60)
    provincia = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.rua}, {self.cidade}, {self.provincia}"

class Empresa(models.Model):
    nif = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone= models.CharField(max_length=16)
    email = models.EmailField(max_length=60)
    website = models.URLField(max_length=60)
    descricao = models.TextField(500)
    id_sector = models.ForeignKey(SectorActividade, on_delete=models.CASCADE)
    id_endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    data_criacao= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

        



   
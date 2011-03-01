from django.db import models



"""
    Classe que armazena informacoes do profile
    de cada usuario.
"""
class Profile(models.Model) :
    pass

ST_GOLD_FILED = (
  (1,'Ativo'),
  (2,'Aguardando Pagamento'),
  (3,'Expirado'),
  (9,'Cancelado'),)

class Gold(models.Model)  : 
    dtcriacao = models.DateTimeField('Data de criacao',auto_now_add=True)
    gold_superior = models.ForeignKey('Gold', blank=True, null=True)
    stgold = models.IntegerField(choices=ST_GOLD_FILED)
    



# Create your models here.

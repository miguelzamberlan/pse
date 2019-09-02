from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Inscricao(models.Model):
    nomeresponsavel = models.CharField(max_length=200)
    cpfresponsavel = models.IntegerField()
    nomecandidato = models.CharField(max_length=200)
    cpfcandidato = models.IntegerField()
    datanascimento = models.DateField()
    endereco = models.CharField(max_length=200)
    endereco_bairro = models.CharField(max_length=200)
    endereco_cidade = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    docidentificacao = models.CharField(max_length=20)
    docidentificacao_emissor = models.CharField(max_length=50)
    nomepai = models.CharField(max_length=200, default=None)
    nomemae = models.CharField(max_length=200, default=None)
    opcaoinscricao = models.CharField(max_length=10)
    em_7_portugues = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    em_8_portugues = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    em_9_portugues = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    em_7_matematica = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    em_8_matematica = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    em_9_matematica = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    em_7_historia = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    em_8_historia = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    em_9_historia = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    em_7_geografia = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    em_8_geografia = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    em_9_geografia = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    em_7_ciencias = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    em_8_ciencias = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    em_9_ciencias = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    provao_portugues = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    provao_matematica = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    provao_historia = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    provao_geografia = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    provao_ciencias = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    encceja_portugues = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    encceja_matematica = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    encceja_historia = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    encceja_geografia = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    encceja_ciencias = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    enem_linguagens = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    enem_matematica = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    outros_portugues = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    outros_matematica = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    outros_historia = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    outros_geografia = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    outros_ciencias = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    media = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    usuarioinseriu = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nomecandidato
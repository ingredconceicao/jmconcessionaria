from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.hashers import make_password


'''Signals -> funciona para inserir algo no banco antes ou depois
        '''
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
        # postado = models.DateField('Data de Postagem', auto_now_add=True)
        disponivel = models.BooleanField('Ativo', default=True)

        class Meta: 
                abstract = True

class Veiculo(Base):

        NOVO = 'novo'
        SEMI_NOVO = 'semi-novo'
        USADO = 'usado'
        condicao_choices = ((NOVO, 'Novo'),(SEMI_NOVO, 'Semi-Novo'), (USADO, 'Usado'),)

        marca = models.CharField('marca', max_length=100)
        modelo = models.CharField('modelo', max_length=100)
        quilometragem = models.DecimalField('quilometragem', max_digits=8, decimal_places=6)
        valor = models.DecimalField('valor',max_digits=8, decimal_places=2)
        ano = models.IntegerField('ano')
        estoque = models.IntegerField('estoque')
        condicao = models.CharField('condicao', max_length=100, choices=condicao_choices)
        imagem = StdImageField('Imagem', upload_to='home', variations={'thumb': (124, 124)})
        slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

        def str(self):
                return self.modelo
        # slugify altera o modelo de ex: Fiat Toro para fiat-toro
def veiculo_pre_save(signal,instance,sender, **kwargs):
        instance.slug = slugify(instance.modelo)
signals.pre_save.connect(veiculo_pre_save, sender=Veiculo)


class Usuario(models.Model):
    cpf = models.CharField(unique=True, max_length=11)



# 
# 
class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.username
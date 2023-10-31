from django.db import models
from stdimage.models import StdImageField

'''Signals -> funciona para inserir algo no banco antes ou depois
        from django.db.models import signals
        from django.template.defaultfilters import slugify'''


class Base(models.Model):
        postado = models.DateField('Data de Postagem', auto_now_add=True)
        modificado = models.DateField('Data de Modificação', auto_created=True)
        disponivel = models.BooleanField('Ativo?', default=True)

        class Meta: 
                abstract = True

# class Veiculo(Base):

#         condicao_choices = (
#                 ('novo', 'Novo',
#                  'semi-novo', 'Semi-novo',
#                  'usado', 'usado',
#                  )
#         )
#         marca = models.CharField('nome', max_length=100)
#         modelo = models.CharField('modelo', max_length=100)
#         quilometragem = models.DecimalField('quilometragem', max_digits=8, decimal_places=6)
#         valor = models.DecimalField('valor',max_digits=8, decimal_places=2)
#         ano = models.IntegerField('ano')
#         estoque = models.IntegerField('estoque')
#         condicao = models.CharField('condicao', max_length=100, choices=condicao_choices)
#         imagem = StdImageField('Imagem', upload_to='home', variations={'thumb': (124, 124)})
#         slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
        
#         def __str__(self):
#                 return self.modelo
# # def veiculo_pre_save(signal,instance,)
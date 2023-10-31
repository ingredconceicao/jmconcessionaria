# Generated by Django 4.2.6 on 2023-10-31 02:45

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modificado', models.DateField(auto_created=True, verbose_name='Data de Modificação')),
                ('postado', models.DateField(auto_now_add=True, verbose_name='Data de Postagem')),
                ('disponivel', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('marca', models.CharField(max_length=100, verbose_name='nome')),
                ('modelo', models.CharField(max_length=100, verbose_name='modelo')),
                ('quilometragem', models.DecimalField(decimal_places=6, max_digits=8, verbose_name='quilometragem')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='valor')),
                ('ano', models.IntegerField(verbose_name='ano')),
                ('estoque', models.IntegerField(verbose_name='estoque')),
                ('condicao', models.CharField(choices=[('novo', 'Novo'), ('semi-novo', 'Semi-Novo'), ('usado', 'Usado')], max_length=100, verbose_name='condicao')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='home', variations={'thumb': (124, 124)}, verbose_name='Imagem')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

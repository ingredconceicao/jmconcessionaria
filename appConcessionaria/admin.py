from django.contrib import admin
from .models import Veiculo


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = (
        "marca",
        "modelo",
        "quilometragem",
        "valor",
        "ano",
        "estoque",
        "condicao",
        "imagem",
        "slug",
        "disponivel",
    )


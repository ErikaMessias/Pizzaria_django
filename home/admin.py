from django.contrib import admin
from .models import Pizzaria

class detPizzaria(admin.ModelAdmin):
    list_display = ('id','titulo','descricao','mostrar','foto')
    list_editable = ('mostrar',)
    list_display_links = ('titulo',)
    search_fields = ('titulo',)
    list_per_page = 2

admin.site.register(Pizzaria, detPizzaria)

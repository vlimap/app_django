from django.contrib import admin
from galeria.models import Fotografia

class Listando(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada", "data")
    list_display_links = ("id", "nome", "legenda")
    search_fields = ("id", "nome", "legenda", "categoria")
    list_filter = ("categoria",)
    list_per_page = 10
    list_editable = ('publicada',)

admin.site.register(Fotografia, Listando)
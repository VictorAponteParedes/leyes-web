from django.contrib import admin

from .models import Caso, Cliente, Abogado, Rolpersona
from django.utils.html import format_html

class CasoAdmin(admin.ModelAdmin):
    list_display = ["nombre","nro_expediente","fecha","materia","juzgado", "foto_perfil"]

admin.site.register(Caso, CasoAdmin)





class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "edad", "telefono", "caso_relacionado", "is_activo", "foto_perfil"]

admin.site.register(Cliente, ClienteAdmin)



class AbogadoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "edad", "telefono", "cliente_relacionado", "foto_perfil"]

    def mostrar_imagen(self, obj):
        if obj.foto_perfil:
            return format_html('<img src="{}" width="50" height="50" />', obj.foto_perfil.url)
        else:
            return format_html('<p>Sin imagen</p>')

    mostrar_imagen.short_description = 'Imagen de Perfil'

admin.site.register(Abogado, AbogadoAdmin)


class RolAdmin(admin.ModelAdmin):
    list_display = ["rol"]


admin.site.register(Rolpersona, RolAdmin)
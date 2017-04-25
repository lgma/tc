from django.contrib import admin

# Register your models here.
from .models import Cliente, Comisionista, Costo, Movimiento, Regreso, Empresa


#admin.site.register(Cliente)
admin.site.register(Comisionista)
admin.site.register(Costo)
admin.site.register(Movimiento)
admin.site.register(Regreso)
admin.site.register(Empresa)


class ClienteAdmin (admin.ModelAdmin):
    list_display = ('id', 'cliente_nombre', 'cliente_calle',
                    'cliente_numext', 'cliente_numint', 'cliente_colonia',
                    'cliente_del_mun', 'cliente_cp', 'cliente_telefono',
                    'cliente_rfc', 'cliente_alta', 'cliente_umodificacion')
    list_filter = ('id', 'cliente_nombre', 'cliente_rfc', 'cliente_telefono')
    search_fields = ('id', 'cliente_rfc', 'cliente_telefono')


admin.site.register(Cliente, ClienteAdmin)
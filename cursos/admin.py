from django.contrib import admin

from cursos.models import Comentarios, Cursos, Aulas, NotasAulas

admin.site.register(Cursos)
admin.site.register(Aulas)
admin.site.register(Comentarios)
admin.site.register(NotasAulas)
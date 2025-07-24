from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Edicao, Noticia, Comentario

admin.site.register(Edicao)
admin.site.register(Noticia)
admin.site.register(Comentario)


    

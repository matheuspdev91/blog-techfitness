from django.contrib import admin
from .models import Post, Categoria
from .models import Comentario

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Comentario)
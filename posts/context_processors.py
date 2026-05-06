from .models import Categoria

def categorias_menu(request):
    categorias = Categoria.objects.all().order_by('nome')
    return {"categorias_menu": categorias}


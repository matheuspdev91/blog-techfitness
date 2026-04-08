from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, Categoria, Comentario
from django.core.management import call_command
from django.http import HttpResponse



def post_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)

    posts =  Post.objects.filter(categoria=categoria).order_by('-criado_em')
    total_posts = posts.count()


    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(request, "posts/lista_posts.html",{
        "page_obj": page_obj,
        "categoria": categoria
    })


def lista_posts(request):

    query = request.GET.get('q', '')

    posts = Post.objects.all().order_by('-criado_em')
    print('total posts:', posts.count())

    if query:
        posts = posts.filter(
            Q(titulo__icontains=query) |
            Q(conteudo__icontains=query)
        )
    
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)


    return render(request, 'posts/lista_posts.html', {
        'page_obj': page_obj,
        'query': query
    })


def post_detail(request, slug):

    post = get_object_or_404(Post, slug=slug)

    return render(request, 'posts/post_detail.html', {
        'post': post
    })

def like_post(request, slug):
    post =  get_object_or_404(Post, slug=slug)
    post.likes += 1
    post.save()
    return redirect('post_detail', slug=slug)

def dislike_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.dislikes += 1
    post.save()
    return redirect('post_detail', slug=slug)

def adicionar_comentario(request, slug):
    post =  get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        conteudo = request.POST.get('conteudo')

        if nome and conteudo:
            Comentario.objects.create(
                post=post,
                nome=nome,
                conteudo=conteudo
            )

    return redirect('post_detail', slug=slug)





def carregar_dados(request):
    call_command('loaddata', 'dados.json')
    return HttpResponse("Dados carregados!")

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q

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

   

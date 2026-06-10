from django.urls import path
from .views import lista_posts, post_detail, post_por_categoria, like_post, dislike_post, adicionar_comentario
from django.conf import settings
from django.conf.urls.static import static
from .views import carregar_dados


urlpatterns =[
    path('', lista_posts, name ='lista_posts'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('categoria/<slug:slug>/', post_por_categoria, name='posts_categoria'),
    path('likes/<slug:slug>/', like_post, name='like_post'),
    path('dislike/<slug:slug>/', dislike_post, name='dislike_post'),
    path('post/<slug:slug>/comentar/', adicionar_comentario, name='adicionar_comentario'),
    path('carregar/', carregar_dados),
    
]

from django.urls import path
from .views import lista_posts, post_detail, post_por_categoria, like_post, dislike_post, adicionar_comentario
from django.conf import settings
from django.conf.urls.static import static
from .views import carregar_dados
from . import views


urlpatterns =[
    path('', lista_posts, name ='lista_posts'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('categoria/<slug:slug>/', post_por_categoria, name='posts_categoria'),
    path('likes/<slug:slug>/', like_post, name='like_post'),
    path('dislike/<slug:slug>/', dislike_post, name='dislike_post'),
    path('post/<slug:slug>/comentar/', adicionar_comentario, name='adicionar_comentario'),
    path('carregar/', carregar_dados),
    path('sobre/', views.sobre,name='sobre')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
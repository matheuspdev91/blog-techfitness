from django.urls import path
from .views import lista_posts, post_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', lista_posts, name ='lista_posts'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
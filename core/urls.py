from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filme/', include('filmes.urls')),
    path('auth/', include('autenticacao.urls')),
    path('', lambda request: redirect('/auth/logar'))

]

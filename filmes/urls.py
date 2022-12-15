from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_filme/', views.cadastrar_filme, name='cadastrar_filme'),
    path('filme_unico/<int:id>', views.filme_unico, name='filme_unico'),
    path('editar_filme/<int:id>', views.editar_filme, name='editar_filme'),
    path('delete/<int:id>/', views.excluir_filme, name='excluir_filme'),

]

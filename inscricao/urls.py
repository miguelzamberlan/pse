from django.urls import path
from . import views
app_name = 'inscricao'

urlpatterns = [
    path('', views.adicionar_inscricao, name='inscricao'),
    path('continuar/', views.continuar_inscricao, name='continuar'),
    path('ficha/<int:id>', views.ficha_inscricao, name='ficha'),
    path('salvar/', views.salvar_inscricao, name='salvar'),
    path('relatorio/', views.relatorio_inscricao, name='relatorio'),
    path('editar/<int:id>/', views.editar_inscricao, name='editar'),
    path('apagar/<int:id>/', views.apagar_inscricao, name='apagar'),
    path('gerarpdf/<int:id>/', views.gerarpdf, name='gerarpdf'),
]
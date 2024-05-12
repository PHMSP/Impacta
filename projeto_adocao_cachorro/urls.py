from django.contrib import admin
from django.urls import path
from app_adocao_cachorro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cadastro_doador/', views.cadastro_doador, name='cadastro_doador'),
    path('cadastro_cachorro/', views.cadastro_cachorro, name='cadastro_cachorro'),
    path('lista_cachorro/', views.lista_cachorro, name='lista_cachorro'),
    path('deletar_cachorro/', views.deletar_cachorro, name='deletar_cachorro'),
]

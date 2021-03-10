from django.urls import include
from django.conf.urls import url
from django.contrib import admin
from .views import *
app_name = 'core'


urlpatterns = [
    url(r'^logar/', logar, name='logar'),
    url(r'^info_list/', listar_info, name='listar_info'),
    url(r'^info_form/', cadastrar_info, name='cadastrar_info'),
    url(r'^info_form/(?P<pk>[0-9]+)', editar_info, name='editar_info'),
    url(r'^tag_list/', listar_tag, name='listar_tag'),
    url(r'^tag_form/', cadastrar_tag, name='cadastrar_tag'),
    url(r'^tag_form/(?P<pk>[0-9]+)', editar_tag, name='editar_tag'),
    url(r'^lembrete_form/', cadastrar_lembrete, name='cadastrar_lembrete'),
    url(r'^lembrete_list/', listar_lembrete, name='listar_lembrete'),
    url(r'^lembrete_form/(?P<pk>[0-9]+)', editar_lembrete, name='editar_lembrete'),
    url(r'^cc_form/', cadastrar_centro_custos, name='cadastrar_centro_custos'),
    url(r'^cc_list/', listar_centro_custos, name='listar_centro_custos'),
    url(r'^cc_form/(?P<pk>[0-9]+)', editar_centro_custos, name='editar_centro_custos'),
    url(r'^status_form/', cadastrar_status, name='cadastrar_status'),
    url(r'^status_list/', listar_status, name='listar_status'),
    url(r'^status_form/(?P<pk>[0-9]+)', editar_status, name='editar_status'),
    #url(r'^perfil_show/(?P<pk>[0-9]+)', perfil_contato, name='perfil_contato'),
    url(r'^perfil_show/', perfil_contato, name='perfil_contato'),
    url(r'^tag/cliente/(?P<pk>[0-9]+)', listar_tag_cliente, name='tag_cliente'),


]
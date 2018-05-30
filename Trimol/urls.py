"""Trimol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')) 
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from Aplicacion.views import prueba,test,Ruta, buscar,contactos,Hospital,Estado,Sector,reporte_uno, Foro, Acerca, Nopermisos,Perfil,list_hospital
from Aplicacion.views import TodasPublicaciones, ListaPublicacion,BuscarView,privado,publicos,datos_hosp

from Aplicacion import views as core_views
from Aplicacion.views import Perfil_View,Perfil_Update,DetallePublicacion

#Prueva dinamic view
from django.conf import settings
from django.conf.urls.static import static

#Para bloquear las url si no estas logueado
#Ej. path('prueba/', login_required(prueba  <-- es la vista),name ='prueba_view'),
from django.contrib.auth.decorators import login_required

#Prueba imagenes
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', core_views.home, name='home'),
    path('', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': 'login'}, name='logout'),
    path('signup/', core_views.SignUp.as_view(), name='signup'),
    
    path('prueba/', prueba,name ='prueba_view'),
    path('test/', test,name ='test_view'),   
    path('ruta/', Ruta,name ='Ruta_view'),   

    path('contactos/', login_required( contactos),name ='contactos_view'),


    path('Hospital/', Hospital, name='Hospital_view'),
    path('Sector/', Sector,name ='Sector_view'),
    path('Estado/', Estado,name ='Estado_view'),

    path('perfil/', Perfil,name ='Perfil'),



    #Reporte
    path('buscar/reporte_all/',reporte_uno, name = "reporte"),

    #Prueva dinamic view
    url(r'^Top',login_required( TodasPublicaciones.as_view()),name='pub-list'),
    url(r'^privado',login_required( privado.as_view()),name='pub-list-privado'),
    url(r'^publicos',login_required( publicos.as_view()),name='pub-list-publicos'),
    #url(r'^entradas/(?P<slug>\w+)$', ListaPublicacion, name='pub-list'),
    url(r'^(?P<pk>\d+)$',DetallePublicacion, name='pub-detail'),
   

   url(r'^busca/$', BuscarView.as_view(), name='busca'),
   #path('busca/',BuscarView.as_view()),   
    path('buscar/',  buscar,name ='Busqueda_view'),
    path('foro/',login_required( Foro),name ='Foro_view'),
    path('acerca/', Acerca,name ='acerca_view'),

	#Login falso
    path('_', Nopermisos, name='Nopermisos_view'),
    path('perfil_view/', Perfil_View.as_view(),name='perfil_view'),

    #Prueba imagen 1.0
    url(r'^list/all/$',list_hospital,name='see_post'),


    url(r'^datos_hosp',datos_hosp.as_view(),name='datos_hosp'),
    url(r'^update_perfil/(?P<pk>[\w-]+)$',Perfil_Update.as_view(),name='update_perfil'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

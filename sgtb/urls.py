from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from sistema import views

app_name = 'sistema'

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),

    # Login
    path('login/', views.loginuser, name='loginuser'),

    # Logout
    path('logout/', views.logoutuser, name='logoutuser'),

    # Gestão de Usuarios
    path('gestaousuarios/', views.gestaousuarios, name='gestaousuarios'),

    # Novo usuario
    path('novousuario/', views.newuser, name='newuser'),

    # Monitoramento
    path('monitoramento/', views.monitoramento, name='monitoramento'),

    # Checkin
    path('checkin/', views.checkin, name='checkin'),

    # Novo Checkin
    path('novocheckin/', views.novocheckin, name='novocheckin'),

    ###
    # passageiro
    ###

    # Passegeiro
    path('checkincliente/', views.checkincliente, name='checkincliente'),

    # Aeroporto
    path('aeroporto/', views.aeroporto, name='aeroporto'),

    # Novo Passegeiro
    path('createpassageiro/', views.createpassageiro, name='createpassageiro'),

    # Rastrear
    path('mala/', views.mala, name='mala'),

        # Ver os To do
    path('minhabagagem/', views.viewmala, name='viewmala'),

]

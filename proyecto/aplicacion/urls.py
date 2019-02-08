from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('jugadores/', views.jugadores, name='jugadores'),
    path('jugadores/<int:pk>', views.jugadorDetalle, name='jugadorDetalle'),
    path('registrarJugador/', views.registrarJugador, name='registrarJugador'),
    path('jugadores/<str:posicion>', views.jugadoresPosicion, name='jugadorPosicion'),
    path('jugadoresDelEquipo/<int:pk>', views.jugadoresDelEquipo, name='jugadoresDelEquipo'),

    path('equipos/', views.equipos, name='equipos'),
    path('equipos/<int:pk>', views.equipoDetalle, name='equipoDetalle'),
    path('registrarEquipo/', views.registrarEquipo, name='registrarEquipo'),

    path('estadios/', views.estadios, name='estadios'),
    path('estadios/<int:pk>', views.estadioDetalle, name='estadioDetalle'),
    path('registrarEstadio/', views.registrarEstadio, name='registrarEstadio'),
]

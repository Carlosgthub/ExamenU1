from django.shortcuts import render, redirect
from .models import Jugador, Equipo, Estadio
from .forms import jugadorForm, equipoForm, estadioForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def jugadores(request):
    lista=Jugador.objects.all()
    equipos=Equipo.objects.all()

    queryset={
        'jugadores':lista,
        'equipos':equipos,
    }

    return render(request, 'jugadores.html', queryset)

def jugadoresPosicion(request, posicion):
    lista=Jugador.objects.filter(posicion=posicion)

    queryset={
        'jugadores':lista
    }

    return render(request, 'jugadoresPosicion.html', queryset)

def jugadorDetalle(request, pk):
    jugador=Jugador.objects.get(id=pk)

    queryset={
        'jugador':jugador
    }

    return render(request, 'jugadorDetalle.html', queryset)

def registrarJugador(request):
    form = jugadorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('jugadores')

    context={
         "form":form
    }
    return render(request,"registro.html",context)

def equipos(request):
    lista=Equipo.objects.all()

    queryset={
        'equipos':lista
    }

    return render(request, 'equipos.html', queryset)

def jugadoresDelEquipo(request, pk):
    lista=Jugador.objects.filter(equipo=pk)

    queryset={
        'jugadores':lista
    }

    return render(request, 'jugadoresDelEquipo.html', queryset)

def equipoDetalle(request, pk):
    equipo=Equipo.objects.get(id=pk)

    queryset={
        'equipo':equipo
    }

    return render(request, 'equipoDetalle.html', queryset)

def registrarEquipo(request):
    form = equipoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('equipos')

    context={
         "form":form
    }
    return render(request,"registro.html",context)

def estadios(request):
    lista=Estadio.objects.all()

    queryset={
        'estadios':lista
    }
    return render(request, 'estadios.html', queryset)

def estadioDetalle(request, pk):
    estadio=Estadio.objects.get(id=pk)

    queryset={
        'estadio':estadio
    }

    return render(request, 'estadioDetalle.html', queryset)

def registrarEstadio(request):
    form = estadioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('estadios')

    context={
         "form":form
    }
    return render(request,"registro.html",context)
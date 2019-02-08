from django import forms
from .models import Jugador, Equipo, Estadio

class jugadorForm(forms.ModelForm):
    nombre=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
    }))

    apellido=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
    }))

    edad=forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
    }))

    POSICION = (
        ('Quarterback', 'Quarterback'),
        ('Wide Receiver ', 'Wide Receiver'),
        ('Running Back', 'Running Back'),
        ('Tight End', 'Tight End'),
        ('Center', 'Center'),
        ('Offensive Guard', 'Offensive Guard'),
        ('Offensive Tackles', 'Offensive Tackles'),
        ('Defensive Tackle', 'Defensive Tackle'),
        ('Defensive End', 'Defensive End'),
        ('Linebacker', 'Linebacker'),
        ('Cornerback', 'Cornerback'),
        ('Safety', 'Safety'),
        ('Kicker', 'Kicker'),
        ('Punter', 'Punter'),
    )

    posicion=forms.ChoiceField(
        choices=POSICION,
        widget=forms.Select(
            attrs={
                "class":"form-control"
            
    }))

    equipo=forms.ModelChoiceField(
        queryset=Equipo.objects.all(),
        widget=forms.Select(
            attrs={
                "class":"form-control"
    }))

    class Meta:
        model = Jugador
        fields='__all__'



class equipoForm(forms.ModelForm):
    nombre=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
    }))

    fundacion=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
    }))

    estadio=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
    }))

    class Meta:
        model = Equipo
        fields='__all__'

class estadioForm(forms.ModelForm):
    nombre=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
    }))

    ciudad=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
    }))

    capacidad=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
    }))

    equipo=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
    }))

    class Meta:
        model = Estadio
        fields='__all__'
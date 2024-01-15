from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Movie


def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

    # return HttpResponse("<h2>Hola Django</h2>")
    # search = request.GET.get('searchMovie')

    # print('buscar:', search)
    # buscar en la base de datos de peliculas
    # return render(request, 'home.html', {'nombre': 'César', 'apellido': 'Alcívar'})



def about(request):
    return render(request, 'about.html')

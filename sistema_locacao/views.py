from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def movie_list(request):
    movies = Movie.objects.filter(rented=False)
    return render(request, 'sistema_locacao/movie_list.html', {'movies': movies})

def rent(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.rented = True
    movie.save()
    return redirect('movie_list')
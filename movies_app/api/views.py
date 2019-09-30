from django.shortcuts import render, redirect
from .models import Movie, People
from .services import sync_db

def home(request):
    response = redirect('/movies')
    return response

def movies(request):
    sync_db()
    c = Movie.objects.all().values("movie_id", "title", "description")
    all_items = []
    for i in c:
        i["people"] = Movie.objects.get(
            movie_id=i["movie_id"]).people.all()
        all_items.append(i)
    return render(request, 'movies.html', {'all_items': all_items})

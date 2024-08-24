from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    help = 'Load movies from movie_descriptions.jason into the Movie model'

    def handle(self, *args, **kwargs):
        #contruct the full path to json file
        #recuerde que la consola esta ubicada en la carpeta djangoprojectbase

        json_file_path = 'movie/management/commands/movies.json'

        # load data from json file

        with open(json_file_path, 'r') as file:
            movies = json.load(file)

        #add products to database
        for i in range(100):
            movie = movies[i]
            exist = Movie.objects.filter(title = movie['title']).first()
            if not exist:
                Movie.objects.create(title = movie['title'],
                                     image = 'movie/images/default.jpg',
                                     genre = movie['genre'],
                                     year = movie['year'],
                                     description = movie['plot'])       
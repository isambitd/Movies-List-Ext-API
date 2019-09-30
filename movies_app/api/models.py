from django.db import models


class People(models.Model):
    people_id = models.CharField(max_length=40, primary_key=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=100)
    hair_color = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):
    movie_id = models.CharField(max_length=40, primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    people = models.ManyToManyField(People)

    def __str__(self):
        return f'{self.title} | {self.description} | {self.people}'

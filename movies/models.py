from django.db import models
from cast.models import Person

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField("created_at",auto_now_add=True)
    updated_at = models.DateTimeField("updated_at",auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="movies"

class Character(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField("created_at",auto_now_add=True)
    updated_at = models.DateTimeField("updated_at",auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="characters"
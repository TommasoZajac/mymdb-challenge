from django.db import models
from reviews.models import Review
from django.contrib.contenttypes.fields import GenericRelation

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.CharField(max_length=1000)
    reviews = GenericRelation(Review)
    created_at = models.DateTimeField("created_at",auto_now_add=True)
    updated_at = models.DateTimeField("updated_at",auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        verbose_name="persons"
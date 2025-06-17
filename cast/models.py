from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.CharField(max_length=1000)
    created_at = models.DateTimeField("created_at",auto_now_add=True)
    updated_at = models.DateTimeField("updated_at",auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        verbose_name="persons"
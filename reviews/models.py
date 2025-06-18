from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q

class Review(models.Model):
    text = models.TextField(max_length=1000)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=Q(
        Q(app_label="movies", model="movie") | Q(app_label="movies", model="character") | Q(app_label="cast", model="person") 
    ))
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField("created_at",auto_now_add=True)
    updated_at = models.DateTimeField("updated_at",auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
        verbose_name="reviews"

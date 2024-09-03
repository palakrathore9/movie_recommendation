from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_year = models.IntegerField(null=True, blank=True)
    genres = models.CharField(max_length=255)
    embedding = models.JSONField()

    def __str__(self):
        return self.title


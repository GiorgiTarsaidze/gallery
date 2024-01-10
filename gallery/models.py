from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    date_of_birth = models.DateField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Artwork(models.Model):
    artist = models.ForeignKey(Artist, related_name='artworks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    creation_date = models.DateField()
    image_url = models.URLField()

    def __str__(self):
        return self.title
    

class Exhibition(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=200)
    artworks = models.ManyToManyField(Artwork)

    def __str__(self):
        return self.name
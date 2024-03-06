from django.db import models

# Create your models here.
class movie (models.Model):
    name = models.CharField(max_length=200)
    Actor_1= models.CharField (max_length = 50)
    Actor_2= models.CharField (max_length = 50)
    Song_1= models.CharField(max_length= 100)
    Song_2= models.CharField(max_length= 100)
    director = models.CharField(max_length =100)
    producer= models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.Actor_1},{self.Actor_2},{self.Song_1},{self.Song_2}{self.director}{self.producer}"
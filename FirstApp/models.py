from django.db import models

# Create your models here.

class FinishedGames(models.Model):
    name = models.CharField(max_length=60)
    release_date = models.CharField(max_length=20)
    rating = models.FloatField()
    
class ProjectsToDo(models.Model):
    name = models.CharField(max_length=40)
    approx_time = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    
class Hobbies(models.Model):
    name = models.CharField(max_length=40)
    

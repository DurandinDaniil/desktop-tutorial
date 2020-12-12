from django.db import models

 
class Review(models.Model):
    text = models.CharField(max_length = 200 )
    length = models.IntegerField(null = True)
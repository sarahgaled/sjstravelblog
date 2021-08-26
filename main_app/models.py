from django.db import models

# Create your models here.

class Blog(models.Model):
    place = models.CharField(max_length=200)
    description = models.TextField(max_length=450)
    date = models.DateField()

    def __str__(self):
        return self.place

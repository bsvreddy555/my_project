from django.db import models

# Create your models here.

class feddback_model(models.Model):
    name=models.CharField(max_length=50)
    rateing=models.FloatField()
    feedback=models.TextField(max_length=200)
    date=models.DateField(max_length=100)

    def __str__(self):
        return self.name

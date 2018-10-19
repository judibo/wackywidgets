from django.db import models

# Create your models here.
class Widget(models.Model):
    description = models.CharField(max_length=500)
    quantity = models.IntegerField()

    def __str__(self):
       return f'{self.description} - {self.quantity}'
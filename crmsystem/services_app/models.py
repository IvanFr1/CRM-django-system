from django.db import models

# Create your models here.


class Services(models.Model):

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return self.name
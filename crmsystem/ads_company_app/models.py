from django.db import models
from services_app.models import Services

# Create your models here.

class Advertise(models.Model):

    name = models.CharField(max_length=100, unique=True)
    ads_service = models.ForeignKey(Services, on_delete=models.CASCADE)
    promote_chanel = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name

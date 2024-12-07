from django.db import models
from services_app.models import Services

# Create your models here.

class Contract(models.Model):

    name = models.CharField(max_length=50)
    provided_service = models.ForeignKey(Services, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self) -> str:
        return self.name


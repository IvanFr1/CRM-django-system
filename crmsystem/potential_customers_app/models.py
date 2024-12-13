from django.db import models
from ads_company_app.models import Advertise

# Create your models here.


class Leads(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    ads_company = models.ForeignKey(
        Advertise, on_delete=models.CASCADE, related_name="leads"
    )
    customer_phone = models.CharField(max_length=15, unique=True)
    customer_email = models.EmailField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

from django.db import models
from potential_customers_app.models import Leads
from contacts_app.models import Contract

# Create your models here.

class Customer(models.Model):

    lead = models.OneToOneField(Leads, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.customer_lead.first_name

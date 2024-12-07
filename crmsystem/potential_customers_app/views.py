from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
    )
from django.urls import reverse_lazy
from .models import Leads

# Create your views here.

class LeadsListView(ListView):

    model = Leads
    template_name = 'potential_customers_app/leads-list.html'
    context_object_name = 'leads'


class LeadsCreateView(CreateView):

    model = Leads
    fields = ['first_name', 'last_name', 'ads_company', 'customer_phone', 'customer_email']
    template_name = 'potential_customers_app/leads-create.html'
    success_url = reverse_lazy('potential_customers_app:leads_list')


class LeadsDetailListView(DetailView):

    model = Leads
    template_name = 'potential_customers_app/leads-detail.html'
    context_object_name = 'leads'


class LeadsDeleteView(DeleteView):

    model = Leads
    success_url = reverse_lazy('potential_customers_app:leads_list')
    template_name = 'potential_customers_app/leads-delete.html'


class LeadsUpdateView(UpdateView):

    model = Leads
    fields = ['first_name', 'last_name', 'ads_company', 'customer_phone', 'customer_email']
    template_name = 'potential_customers_app/leads-edit.html'
    success_url = reverse_lazy('potential_customers_app:leads_list')

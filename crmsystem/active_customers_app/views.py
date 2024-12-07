from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
    )
from django.urls import reverse_lazy
from .models import Customer

# Create your views here.

class CustomersListView(ListView):

    model = Customer
    template_name = 'active_customers_app/customers-list.html'
    context_object_name = 'customers'


class CustomersCreateView(CreateView):

    model = Customer
    fields = ['lead', 'contract']
    template_name = 'active_customers_app/customers-create.html'
    success_url = reverse_lazy('active_customers_app:customers_list')


class CustomersDetailListView(DetailView):

    model = Customer
    template_name = 'active_customers_app/customers-detail.html'
    context_object_name = 'customers'


class CustomersDeleteView(DeleteView):

    model = Customer
    success_url = reverse_lazy('active_customers_app:customers_list')
    template_name = 'active_customers_app/customers-delete.html'


class CustomersUpdateView(UpdateView):

    model = Customer
    fields = ['lead', 'contract']
    template_name = 'active_customers_app/customers-edit.html'
    success_url = reverse_lazy('active_customers_app:customers_list')

from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
    )
from django.urls import reverse_lazy
from .models import Contract

# Create your views here.

class ContractListView(ListView):

    model = Contract
    template_name = 'contacts_app/contracts-list.html'
    context_object_name = 'contracts'


class ContractCreateView(CreateView):

    model = Contract
    fields = [
        'name', 
        'provided_service', 
        'file', 
        'start_date', 
        'end_date',
        'cost',
        ]
    template_name = 'contacts_app/contracts-create.html'
    success_url = reverse_lazy('contacts_app:contracts_list')


class ContractDetailListView(DetailView):

    model = Contract
    template_name = 'contacts_app/contracts-detail.html'
    context_object_name = 'contracts'


class ContractDeleteView(DeleteView):

    model = Contract
    success_url = reverse_lazy('contacts_app:contracts_list')
    template_name = 'contacts_app/contracts-delete.html'


class ContractUpdateView(UpdateView):

    model = Contract
    fields = [
        'name', 
        'provided_service', 
        'file', 
        'start_date', 
        'end_date',
        'cost',
        ]
    template_name = 'contacts_app/contracts-edit.html'
    success_url = reverse_lazy('contacts_app:contracts_list')

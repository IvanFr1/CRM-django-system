from django.shortcuts import render
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
    )
from django.urls import reverse_lazy
from .models import Services

# Create your views here.

class ServiceListView(ListView):

    model = Services
    template_name = 'services_app/products-list.html'
    context_object_name = 'products'


class ServiceCreateView(CreateView):

    model = Services
    fields = ['name', 'description', 'cost']
    template_name = 'services_app/products-create.html'
    success_url = reverse_lazy('services_app:products_list')


class ServiceDetailListView(DetailView):

    model = Services
    template_name = 'services_app/products-detail.html'
    context_object_name = 'products'


class ServiceDeleteView(DeleteView):

    model = Services
    success_url = reverse_lazy('services_app:products_list')
    template_name = 'services_app/products-delete.html'


class ServiceUpdateView(UpdateView):

    model = Services
    fields = ['name', 'description', 'cost']
    template_name = 'services_app/products-edit.html'
    success_url = reverse_lazy('services_app:products_list')
    
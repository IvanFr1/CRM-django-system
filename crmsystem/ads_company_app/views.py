from django.shortcuts import render
from django.db.models import Count, Sum, ExpressionWrapper, DecimalField, F
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
    )
from django.urls import reverse_lazy
from .models import Advertise

# Create your views here.

class AdveriseListView(ListView):

    model = Advertise
    template_name = 'ads_company_app/ads-list.html'
    context_object_name = 'ads'


class AdvertiseCreateView(CreateView):

    model = Advertise
    fields = ['name', 'ads_service', 'promote_chanel', 'budget']
    template_name = 'ads_company_app/ads-create.html'
    success_url = reverse_lazy('ads_company_app:ads_list')


class AdvertiseDetailListView(DetailView):

    model = Advertise
    template_name = 'ads_company_app/ads-detail.html'
    context_object_name = 'ads'


class AdvertiseDeleteView(DeleteView):

    model = Advertise
    success_url = reverse_lazy('ads_company_app:ads_list')
    template_name = 'ads_company_app/ads-delete.html'


class AdvertiseUpdateView(UpdateView):

    model = Advertise
    fields = ['name', 'ads_service', 'promote_chanel', 'budget']
    template_name = 'ads_company_app/ads-edit.html'
    success_url = reverse_lazy('ads_company_app:ads_list')


class StatisticListView(ListView):

    model = Advertise
    template_name = 'ads_company_app/ads-statistic.html'
    context_object_name = 'ads'

    def get_queryset(self):

        queryset = Advertise.objects.prefetch_related(
            'leads__customer__contract'
        ).annotate(
            leads_count=Count('leads'),
            customers_count=Count('leads__customer', distinct=True),
            profit=ExpressionWrapper(
                Sum('leads__customer__contract__cost') - F('budget'),
                output_field=DecimalField(max_digits=10, decimal_places=2)
            ),
        )
        return queryset
    
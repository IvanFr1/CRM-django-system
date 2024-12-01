from django.urls import path
from .views import (
    ServiceCreateView, 
    ServiceListView,
    ServiceDetailListView,
    ServiceDeleteView,
    ServiceUpdateView,
    )

app_name = 'services_app'


urlpatterns = [
    path('', ServiceListView.as_view(), name='products_list'),
    path('new/', ServiceCreateView.as_view(), name='products_create'),
    path('<int:pk>', ServiceDetailListView.as_view(), name='products_detail'),
    path('<int:pk>/delete/', ServiceDeleteView.as_view(), name='products_delete'),
    path('<int:pk>/edit/', ServiceUpdateView.as_view(), name='products_edit'),
]
from django.urls import path
from .views import (
    CustomersCreateView, 
    CustomersListView,
    CustomersDetailListView,
    CustomersDeleteView,
    CustomersUpdateView,
    )

app_name = 'active_customers_app'


urlpatterns = [
    path('', CustomersListView.as_view(), name='customers_list'),
    path('new/', CustomersCreateView.as_view(), name='customers_create'),
    path('<int:pk>', CustomersDetailListView.as_view(), name='customers_detail'),
    path('<int:pk>/delete/', CustomersDeleteView.as_view(), name='customers_delete'),
    path('<int:pk>/edit/', CustomersUpdateView.as_view(), name='customers_edit'),
]

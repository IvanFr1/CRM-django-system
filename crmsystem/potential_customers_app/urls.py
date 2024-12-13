from django.urls import path
from .views import (
    LeadsCreateView,
    LeadsListView,
    LeadsDetailListView,
    LeadsDeleteView,
    LeadsUpdateView,
)

app_name = "potential_customers_app"


urlpatterns = [
    path("", LeadsListView.as_view(), name="leads_list"),
    path("new/", LeadsCreateView.as_view(), name="leads_create"),
    path("<int:pk>", LeadsDetailListView.as_view(), name="leads_detail"),
    path("<int:pk>/delete/", LeadsDeleteView.as_view(), name="leads_delete"),
    path("<int:pk>/edit/", LeadsUpdateView.as_view(), name="leads_edit"),
]

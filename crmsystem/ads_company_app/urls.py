from django.urls import path
from .views import (
    AdvertiseCreateView,
    AdveriseListView,
    AdvertiseDetailListView,
    AdvertiseDeleteView,
    AdvertiseUpdateView,
    StatisticListView,
)

app_name = "ads_company_app"


urlpatterns = [
    path("", AdveriseListView.as_view(), name="ads_list"),
    path("new/", AdvertiseCreateView.as_view(), name="ads_create"),
    path("<int:pk>", AdvertiseDetailListView.as_view(), name="ads_detail"),
    path("<int:pk>/delete/", AdvertiseDeleteView.as_view(), name="ads_delete"),
    path("<int:pk>/edit/", AdvertiseUpdateView.as_view(), name="ads_edit"),
    path("statistic/", StatisticListView.as_view(), name="ads_statistic"),
]

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ContractCreateView, 
    ContractListView,
    ContractDetailListView,
    ContractDeleteView,
    ContractUpdateView,
    )

app_name = 'contacts_app'


urlpatterns = [
    path('', ContractListView.as_view(), name='contracts_list'),
    path('new/', ContractCreateView.as_view(), name='contracts_create'),
    path('<int:pk>', ContractDetailListView.as_view(), name='contracts_detail'),
    path('<int:pk>/delete/', ContractDeleteView.as_view(), name='contracts_delete'),
    path('<int:pk>/edit/', ContractUpdateView.as_view(), name='contracts_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

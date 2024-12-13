"""
URL configuration for crmsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("auth_users.urls")),
    path("products/", include("services_app.urls")),
    path("ads/", include("ads_company_app.urls")),
    path("leads/", include("potential_customers_app.urls")),
    path("contracts/", include("contacts_app.urls")),
    path("customers/", include("active_customers_app.urls")),
]

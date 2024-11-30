from django.urls import path
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from .views import MyLogoutView

app_name = 'auth_users'


urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='auth_users/login.html',
        redirect_authenticated_user=True,
        ),
          name='login'
        ),
    path('base/', TemplateView.as_view(template_name='auth_users/_base.html'), name='base'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]
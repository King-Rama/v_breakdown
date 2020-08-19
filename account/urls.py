from django.urls import path, include
from . import views

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('', views.client_register, name='client-register'),
]

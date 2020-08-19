from django.urls import path

from garage import views

app_name = 'garage'

urlpatterns = [
    path('home/', views.GarageHome.as_view(), name='home'),
    path('update/', views.GarageUpdateView.as_view(), name='update'),
    path('request/cancelled/', views.TripListViewCancelled.as_view(), name='trip-cancelled'),
    path('request/cancelled/', views.TripListViewSuccess.as_view(), name='trip-success'),
    path('request/success/', views.Trip.as_view(), name='trips'),
]

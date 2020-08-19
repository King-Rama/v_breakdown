from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('home/', views.home_page, name='index_page'),
    path('emergency/', views.EmergenceCreateView.as_view(), name='emergency'),
    path('request/detail/<int:pk>/', views.EmergenceDetailView.as_view(), name='emergency-detail'),
    path('request/cancelled/', views.TripListViewCancelled.as_view(), name='trip_canceled'),
    path('request/finished/', views.TripListViewSuccess.as_view(), name='trip_finished'),
    path('requests/', views.TripListViewCancelled.as_view(), name='trips'),
    path('profile/update/', views.EditProfile.as_view(), name='client_update'),
    path('change-password/', views.change_password, name='pass_change'),
    path('statistics/', views.Statics.as_view(), name='statics'),
    path('user-detail/', views.ClientDetailView.as_view(), name='user-detail'),
]

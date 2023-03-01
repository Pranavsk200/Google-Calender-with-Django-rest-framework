from django.urls import path
from . import views


urlpatterns = [
    path('google_oauth', views.google_oauth, name='google_oauth'),
    path('v1/calendar/init/', views.GoogleCalendarInitView, name='google_permission'),
    path('v1/calendar/redirect/', views.GoogleCalendarRedirectView, name='google_redirect')
]
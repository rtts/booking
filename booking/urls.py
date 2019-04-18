from django.urls import path
from .views import Welcome, Schedule

app_name = 'booking'

urlpatterns = [
    path('<slug:slug>/', Welcome.as_view(), name='welcome'),
    path('<slug:slug>/add/', Schedule.as_view(), name='schedule'),
]

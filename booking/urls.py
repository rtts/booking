from django.urls import path
from django.shortcuts import redirect
from .views import Welcome, Schedule

app_name = 'booking'

def homepage(request):
    return redirect('http://www.superformosa.nl/')

urlpatterns = [
    path('', homepage),
    path('<slug:slug>/', Welcome.as_view(), name='welcome'),
    path('<slug:slug>/add/', Schedule.as_view(), name='schedule'),
]

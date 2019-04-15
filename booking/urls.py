from django.urls import path
from .views import Welcome, Success

app_name = 'booking'

urlpatterns = [
    path('<slug:slug>/', Welcome.as_view(), name='welcome'),
    path('<slug:slug>/success/', Success.as_view(), name='success'),
]

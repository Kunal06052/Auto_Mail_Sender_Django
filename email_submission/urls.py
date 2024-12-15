from django.urls import path
from .views import submit_assignment, home

urlpatterns = [
    path('', home, name='home'),
    path('submit/', submit_assignment, name='submit_assignment'),
]
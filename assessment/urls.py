from django.urls import path
from .views import questionnaire

urlpatterns = [
    path('dashboard/', questionnaire, name='dashboard'),
]
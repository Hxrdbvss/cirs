from django.urls import path
from . import views

app_name = 'survey_creator'  # Пространство имен для URL

urlpatterns = [
    path('create/', views.create_survey, name='create_survey'),
]
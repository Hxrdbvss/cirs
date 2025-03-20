from django.urls import path
from . import views

app_name = 'polls'  # Пространство имен

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:survey_id>/', views.detail, name='detail'),
    path('<int:survey_id>/vote/', views.vote, name='vote'),
    path('<int:survey_id>/results/', views.results, name='results'),
]
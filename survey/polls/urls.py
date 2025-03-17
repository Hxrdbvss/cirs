from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:survey_id>/', views.detail, name='detail'),
    path('<int:survey_id>/vote/', views.vote, name='vote'),
    path('<int:survey_id>/results/', views.results, name='results'),  # Этот маршрут нужен
]
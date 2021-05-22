from django.urls import path

from . import views

urlpatterns = [
    path('charts/', views.display_charts, name='tariff-charts'),
]

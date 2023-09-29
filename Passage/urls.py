from django.urls import path
from Passage import views

urlpatterns = [
    path('get/', views.list)
]
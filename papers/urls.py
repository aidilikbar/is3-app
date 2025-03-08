from django.urls import path
from .views import search_papers, paper_details

urlpatterns = [
    path("search/", search_papers, name="search_papers"),
    path("details/<str:paper_id>/", paper_details, name="paper_details"),
]
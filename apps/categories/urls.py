from django.urls import path
from .views import CategoriesListView,CategoriesCreateView,CategoriesDetailView
 
 
urlpatterns = [
    path("categories/",CategoriesListView.as_view(),name="categories"),
    path("categories/create/", CategoriesCreateView.as_view(),name="categories-create"),
    path("categories/<int:id>/", CategoriesDetailView.as_view(),name="categories-id")
]
 
from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/comments/", views.comments, name="comments"),
    path("create/", views.create, name="create"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/like/", views.like, name="like"),
    path("category/<str:val>/", views.category, name="category"),
]

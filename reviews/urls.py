from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/comments/", views.comments, name="comments"),
    path("create/", views.create, name="create"),
    path('<int:pk>/like/', views.like, name='like'),
]

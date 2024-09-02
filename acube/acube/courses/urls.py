from django.urls import path
from . import views

urlpatterns= [
    path("frontend/", views.index, name="frontend"),
    path("fullstack/",views.fullstack),
    path("backend/",views.backend)
]
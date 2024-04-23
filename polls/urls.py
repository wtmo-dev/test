from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "ak/",
        views.aaa.as_view(),
    ),
]
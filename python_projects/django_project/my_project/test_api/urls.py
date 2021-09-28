from django.urls import path
from . import views
from .apps import TestApiConfig as Config

app_name = Config.name

urlpatterns = [
    path(
        "student-list",
        views.StudentList.as_view(),
        name = "student_request",

    ),
]

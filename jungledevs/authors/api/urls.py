from django.urls import path

from jungledevs.authors.api.views import (
    CreateAuthorsView,
    ListAuthorsView,
    RetrieveUpdateDestroyAuthorsView,
)

app_name = "admin"

urlpatterns = [
    path("authors/", ListAuthorsView.as_view(), name="list-authors"),
    path("authors/create/", CreateAuthorsView.as_view(), name="create-author"),
    path("authors/update/<int:pk>/", RetrieveUpdateDestroyAuthorsView.as_view(), name="update-destroy-author"),
]

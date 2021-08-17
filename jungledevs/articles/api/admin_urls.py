from django.urls import path

from jungledevs.articles.api.views import (
    CreateArticleView,
    ListArticleView,
    RetrieveUpdateDestroyArticleView,
)

app_name = "admin"

urlpatterns = [
    path("articles/", ListArticleView.as_view(), name="list-articles"),
    path("articles/create/", CreateArticleView.as_view(), name="create-articles"),
    path("articles/update/<int:pk>/", RetrieveUpdateDestroyArticleView.as_view(), name="update-destroy-articles"),
    path("category/", ListArticleView.as_view(), name="list-articles"),
    path("category/create/", CreateArticleView.as_view(), name="create-articles"),
    path("category/update/<int:pk>/", RetrieveUpdateDestroyArticleView.as_view(), name="update-destroy-articles"),
]

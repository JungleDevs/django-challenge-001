from django.urls import path

from jungledevs.articles.api.views import (
    CreateArticleView,
    CreateCategoryView,
    ListArticleView,
    ListCategoryView,
    RetrieveUpdateDestroyArticleView,
    RetrieveUpdateDestroyCategoryView,
)

app_name = "admin"

urlpatterns = [
    path("articles/", ListArticleView.as_view(), name="list-articles"),
    path("articles/create/", CreateArticleView.as_view(), name="create-articles"),
    path("articles/update/<int:pk>/", RetrieveUpdateDestroyArticleView.as_view(), name="update-destroy-articles"),
    path("category/", ListCategoryView.as_view(), name="list-articles"),
    path("category/create/", CreateCategoryView.as_view(), name="create-articles"),
    path("category/update/<int:pk>/", RetrieveUpdateDestroyCategoryView.as_view(), name="update-destroy-articles"),
]

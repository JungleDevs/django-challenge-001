from django.urls import path

from jungledevs.articles.api.views import ArticleDetailView, ArticleSearchView

app_name = "articles"

urlpatterns = [
    path("<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("", ArticleSearchView.as_view(), name="article-search"),
]

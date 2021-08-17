from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from jungledevs.articles.api.serializers import (
    AdminArticlesSerializer,
    AnonymousSerializer,
    LoggedSerializer,
    SearchArticleSerializer,
)
from jungledevs.articles.models import Article, Category


class BaseAdminArticleView(object):
    queryset = Article.objects.all()
    serializer_class = AdminArticlesSerializer
    permission_classes = (IsAdminUser,)


class CreateArticleView(BaseAdminArticleView, CreateAPIView):
    pass


class ListArticleView(BaseAdminArticleView, ListAPIView):
    pass


class RetrieveUpdateDestroyArticleView(BaseAdminArticleView, RetrieveUpdateDestroyAPIView):
    pass


class BaseAdminCategoryView(object):
    queryset = Category.objects.all()
    serializer_class = AdminArticlesSerializer
    permission_classes = (IsAdminUser,)


class CreateCategoryView(BaseAdminCategoryView, CreateAPIView):
    pass


class ListCategoryView(BaseAdminCategoryView, ListAPIView):
    pass


class RetrieveUpdateDestroyCategoryView(BaseAdminCategoryView, RetrieveUpdateDestroyAPIView):
    pass


class ArticleDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return LoggedSerializer
        return AnonymousSerializer


class ArticleSearchView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    search_fields = ["category__name"]
    filter_backends = [DjangoFilterBackend]
    serializer_class = SearchArticleSerializer
    queryset = Article.objects.all()

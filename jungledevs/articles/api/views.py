from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from jungledevs.articles.api.serializers import (
    AdminArticlesSerializer,
    AdminCategorySerializer,
    AnonymousSerializer,
    LoggedSerializer,
    SearchArticleSerializer,
)
from jungledevs.articles.models import Article, Category


class BaseAdminArticleView(object):
    queryset = Article.objects.all().order_by("id")
    serializer_class = AdminArticlesSerializer
    permission_classes = (IsAdminUser,)


class CreateArticleView(BaseAdminArticleView, CreateAPIView):
    pass


class ListArticleView(BaseAdminArticleView, ListAPIView):
    pass


class RetrieveUpdateDestroyArticleView(BaseAdminArticleView, RetrieveUpdateDestroyAPIView):
    pass


class BaseAdminCategoryView(object):
    queryset = Category.objects.all().order_by("id")
    serializer_class = AdminCategorySerializer
    permission_classes = (IsAdminUser,)


class CreateCategoryView(BaseAdminCategoryView, CreateAPIView):
    pass


class ListCategoryView(BaseAdminCategoryView, ListAPIView):
    pass


class RetrieveUpdateDestroyCategoryView(BaseAdminCategoryView, RetrieveUpdateDestroyAPIView):
    pass


class ArticleDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Article.objects.all().order_by("id")

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return LoggedSerializer
        return AnonymousSerializer


class ArticleSearchView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SearchArticleSerializer
    lookup_url_kwarg = "category"

    def get_queryset(self):
        return Article.objects.filter(category__name=self.request.query_params.get("category")).order_by("id")

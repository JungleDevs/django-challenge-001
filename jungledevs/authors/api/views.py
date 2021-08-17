from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser

from jungledevs.authors.api.serializers import AuthorsSerializer
from jungledevs.authors.models import Author


class BaseAuthorsView(object):
    queryset = Author.objects.all()
    serializer_class = AuthorsSerializer
    permission_classes = (IsAdminUser,)


class CreateAuthorsView(BaseAuthorsView, CreateAPIView):
    pass


class ListAuthorsView(BaseAuthorsView, ListAPIView):
    pass


class RetrieveUpdateDestroyAuthorsView(BaseAuthorsView, RetrieveUpdateDestroyAPIView):
    pass

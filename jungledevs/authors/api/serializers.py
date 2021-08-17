from rest_framework.serializers import ModelSerializer

from jungledevs.authors.models import Author


class AuthorsSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "picture"]

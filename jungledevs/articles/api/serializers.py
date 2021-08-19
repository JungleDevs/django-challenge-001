from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from jungledevs.articles.models import Article, Category


class AdminArticlesSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            "id",
            "author",
            "category",
            "title",
            "summary",
            "firstParagraph",
            "body",
        ]


class AdminCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class AnonymousSerializer(ModelSerializer):
    author = SerializerMethodField()
    category = CharField(source="category.name")

    class Meta:
        model = Article
        fields = [
            "id",
            "author",
            "category",
            "title",
            "summary",
            "firstParagraph",
        ]

    def get_author(self, obj):
        article_author = {"id": obj.author.pk, "name": obj.author.name, "picture": obj.author.picture}

        return article_author


class LoggedSerializer(ModelSerializer):
    author = SerializerMethodField()
    category = CharField(source="category.name")

    class Meta:
        model = Article
        fields = [
            "id",
            "author",
            "category",
            "title",
            "summary",
            "firstParagraph",
            "body",
        ]

    def get_author(self, obj):
        article_author = {"id": obj.author.pk, "name": obj.author.name, "picture": obj.author.picture}

        return article_author


class SearchArticleSerializer(ModelSerializer):
    author = SerializerMethodField()
    category = CharField(source="category.name")

    class Meta:
        model = Article
        fields = [
            "id",
            "author",
            "category",
            "title",
            "summary",
        ]

    def get_author(self, obj):
        article_author = {"id": obj.author.pk, "name": obj.author.name, "picture": obj.author.picture}

        return article_author

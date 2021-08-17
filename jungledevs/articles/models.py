from django.db.models import (
    CASCADE,
    PROTECT,
    CharField,
    ForeignKey,
    QuerySet,
    SlugField,
)
from django.utils.translation import ugettext_lazy as _

from jungledevs.utils.base_model import BaseModel


class Article(BaseModel):
    author = ForeignKey("authors.Author", on_delete=CASCADE, verbose_name=_("Author ID"))
    category = ForeignKey("Category", on_delete=PROTECT, verbose_name=_("Category ID"))
    title = CharField(max_length=30, verbose_name=_("Title"))
    summary = CharField(max_length=100, verbose_name=_("Summary"))
    firstParagraph = CharField(max_length=100, verbose_name=_("First Paragraph"))
    body = CharField(max_length=100, verbose_name=_("Body"))
    objects = QuerySet.as_manager()

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")


class Category(BaseModel):
    name = SlugField(verbose_name=_("Name"), unique=True)
    objects = QuerySet.as_manager()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

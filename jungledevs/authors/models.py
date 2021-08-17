from django.db.models import CharField, QuerySet, URLField
from django.utils.translation import ugettext_lazy as _

from jungledevs.utils.base_model import BaseModel


class Author(BaseModel):
    name = CharField(max_length=100, verbose_name=_("Name"))
    picture = URLField(verbose_name=_("Picture"))
    objects = QuerySet.as_manager()

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

from django.db.models import DateTimeField, Model
from django.utils.translation import ugettext_lazy as _


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True, verbose_name=_("Creation Date"))
    updated_at = DateTimeField(auto_now=True, verbose_name=_("Update Date"))

    class Meta:
        abstract = True

    def is_new(self) -> bool:
        """
        There could be a few microseconds of difference between created_at and updated_at of newly created records.
        This code ignores that difference.
        :return:
        """
        return self.created_at.replace(microsecond=0) == self.updated_at.replace(microsecond=0)

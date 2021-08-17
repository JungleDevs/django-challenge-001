from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import CharField, DateField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

PHONE_MAX_LENGTH = 11
PHONE_MIN_LENGTH = 10


class User(AbstractUser):
    birth_date = DateField(verbose_name=_("Date of Birth"), blank=True, null=True)
    phone = CharField(max_length=PHONE_MAX_LENGTH, verbose_name=_("Phone"), blank=True, null=True)
    objects = UserManager()

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

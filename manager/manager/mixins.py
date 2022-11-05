from django.db import models
from django.utils.translation import gettext_lazy as _

class DateTimeMixinModel():
    date_created = models.DateTimeField(_("date created"),auto_now_add=True, blank=True, null=True)
    date_update = models.DateTimeField(_("date update"),auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True

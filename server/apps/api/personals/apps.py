from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PersonalsConfig(AppConfig):
    """Default app config"""

    name = "apps.api.personals"
    verbose_name = _("Personals")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import

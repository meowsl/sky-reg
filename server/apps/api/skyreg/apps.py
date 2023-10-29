from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SkyregConfig(AppConfig):
    """Default app config"""

    name = "apps.api.skyreg"
    verbose_name = _("Skyreg")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import

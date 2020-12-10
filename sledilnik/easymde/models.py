from django.db import models
from django.contrib.admin import widgets as admin_widgets

from .forms import MarkdownFormField
from .widgets import MarkdownWidget, AdminMarkdownWidget


class MarkdownField(models.TextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            "widget": MarkdownWidget,
            "form_class": MarkdownFormField
        }

        defaults.update(kwargs)

        if defaults["widget"] == admin_widgets.AdminTextareaWidget:
            defaults["widget"] = AdminMarkdownWidget()

        return super().formfield(**defaults)

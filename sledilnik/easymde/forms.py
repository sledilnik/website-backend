from django.forms import CharField

from .widgets import MarkdownWidget


class MarkdownFormField(CharField):
    widget = MarkdownWidget

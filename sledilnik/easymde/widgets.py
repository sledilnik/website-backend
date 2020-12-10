import uuid

from django.forms import widgets
from django.contrib.admin import widgets as admin_widgets


class MarkdownWidget(widgets.Textarea):
    template_name = "easymde/forms/widgets/markdown.html"

    def __init__(self, options=None, **kwargs):
        super().__init__(**kwargs)
        self.options = {} if options is None else options

    def get_context(self, *args):
        context = super().get_context(*args)
        context.update({
            "options": self.options,
            "options_id": uuid.uuid4().hex
        })
        return context

    class Media:
        js = ("https://unpkg.com/easymde/dist/easymde.min.js",)

        css = {
            "all": (
                "https://unpkg.com/easymde/dist/easymde.min.css",
                "/static/easymde/easymde.css"
            )
        }


class AdminMarkdownWidget(MarkdownWidget, admin_widgets.AdminTextareaWidget):
    pass

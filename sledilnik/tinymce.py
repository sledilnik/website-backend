import datetime
from pathlib import Path

from django.conf import settings
from django.db import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.files.storage import default_storage as storage
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.contrib.admin import widgets as admin_widgets

from tinymce import widgets as tinymce_widgets


class HTMLField(models.TextField):
    """A text field for HTML content. It uses the TinyMCE widget in forms."""

    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop('options', {})
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {"widget": tinymce_widgets.TinyMCE(mce_attrs=self.options)}
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        if defaults["widget"] == admin_widgets.AdminTextareaWidget:
            defaults["widget"] = tinymce_widgets.AdminTinyMCE(mce_attrs=self.options)

        return super().formfield(**defaults)


ALLOWED_IMAGE_TYPES = [
    "image/gif",
    "image/jpg",
    "image/jpeg",
    "image/pjpeg",
    "image/png",
    "image/x-png",
    "image/webp"
]


@csrf_exempt
@require_POST
@login_required
def upload(request):
    print(request.META.get("HTTP_REFERER"))
    if "file" in request.FILES:
        file = request.FILES["file"]
        if request.FILES.get("type") == "image" and file.content_type not in ALLOWED_IMAGE_TYPES:
            return JsonResponse({"error": _("The uploaded file is not an image.")})

        upload_to = datetime.datetime.now().strftime(settings.TINYMCE_UPLOAD_TO)
        upload_path = storage.save(Path(upload_to, file.name), file)

        return JsonResponse({"location": storage.url(upload_path)})

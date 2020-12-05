from django.contrib import admin

from sledilnik.utils import TranslationAdmin

from . import models


@admin.register(models.Post)
class Post(TranslationAdmin):
    list_display = ["published", "title", "created", "updated"]
    list_display_links = ["title"]
    search_fields = ["author", "title", "blurb", "body"]

    class Media:
        js = ["scripts/tinymce-file-picker.js"]

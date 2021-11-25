from adminsortable2.admin import SortableInlineAdminMixin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from django.contrib import admin

from . import models


class MediaMixin:

    js = (
        'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
        'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        'modeltranslation/js/tabbed_translation_fields.js',
    )
    css = {
        'screen': (
            'modeltranslation/css/tabbed_translation_fields.css',
            'faq/admin/easymde.css',
        ),
    }


class FaqInline(SortableInlineAdminMixin, TranslationStackedInline):
    model = models.Faq
    extra = 0


class GlossaryTermInline(SortableInlineAdminMixin, TranslationStackedInline):
    model = models.GlossaryTerm
    extra = 0


@admin.register(models.Project)
class ProjectAdmin(TranslationAdmin):
    inlines = [FaqInline, GlossaryTermInline]

    class Media(MediaMixin):
        pass

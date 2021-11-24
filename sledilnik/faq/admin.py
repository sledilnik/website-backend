from adminsortable2.admin import SortableInlineAdminMixin
from modeltranslation.admin import TranslationStackedInline

from django.contrib import admin

from sledilnik.utils import TranslationAdmin

from . import models


class FaqInline(SortableInlineAdminMixin, TranslationStackedInline):
    model = models.Faq
    extra = 0


@admin.register(models.Project)
class ProjectAdmin(TranslationAdmin):
    inlines = [FaqInline]

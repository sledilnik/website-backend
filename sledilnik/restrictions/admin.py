from django.contrib import admin
from sledilnik.utils import TranslationAdmin
from adminsortable2.admin import SortableAdminMixin

from .models import Restriction

# Register your models here.
@admin.register(Restriction)
class RestrictionAdmin(SortableAdminMixin, TranslationAdmin):
    list_display = ['title', 'regions', 'valid_since', 'valid_until', 'published']
    # ordering = ('-order',)

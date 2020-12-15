from modeltranslation.translator import register, TranslationOptions
from .models import Restriction


@register(Restriction)
class RestrictionTranslationOptions(TranslationOptions):
    fields = ["title", "rule", "regions", "exceptions", "extra_rules", "validity_comment", "comments"]

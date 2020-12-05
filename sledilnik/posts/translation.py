from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Post)
class PostTranslationOptions(TranslationOptions):
    fields = ["author", "title", "blurb", "link_to", "body"]

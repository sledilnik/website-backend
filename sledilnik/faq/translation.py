from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ["name"]


@register(models.Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ["slug", "question", "answer"]
    empty_values = {"slug": None}


@register(models.GlossaryTerm)
class GlossaryTermTranslationOptions(TranslationOptions):
    fields = ["slug", "term", "definition"]
    empty_values = {"slug": None}

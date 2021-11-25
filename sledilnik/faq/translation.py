from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = []


@register(models.Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ["question", "answer"]


@register(models.GlossaryTerm)
class GlossaryTermTranslationOptions(TranslationOptions):
    fields = ["term", "definition"]
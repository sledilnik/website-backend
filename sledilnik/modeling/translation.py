from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Model)
class ModelTranslationOptions(TranslationOptions):
    fields = ["name", "www", "description"]


@register(models.Scenario)
class ScenarioTranslationOptions(TranslationOptions):
    fields = ["name", "description"]


@register(models.IntervalKind)
class IntervalKindTranslationOptions(TranslationOptions):
    fields = ["name", "description"]

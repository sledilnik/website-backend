from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Model)
class ModelTranslationOptions(TranslationOptions):
    fields = ["name", "www", "description"]


@register(models.Scenario)
class ScenarioTranslationOptions(TranslationOptions):
    fields = ["name", "description"]


@register(models.PredictionIntervalType)
class PredictionIntervalTypeTranslationOptions(TranslationOptions):
    fields = ["name", "description"]

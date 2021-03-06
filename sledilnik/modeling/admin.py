from django.contrib import admin

from sledilnik.utils import TranslationAdmin

from . import models


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    list_display_links = ["name"]


@admin.register(models.Model)
class ModelAdmin(TranslationAdmin):
    list_display = ["active", "name", "id"]
    list_display_links = ["name"]
    filter_horizontal = ["contacts"]


@admin.register(models.Scenario)
class ScenarioAdmin(TranslationAdmin):
    list_display = ["name"]
    list_display_links = ["name"]


@admin.register(models.IntervalKind)
class IntervalKindAdmin(TranslationAdmin):
    list_display = ["name"]
    list_display_links = ["name"]


@admin.register(models.Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ["date", "model", "scenario", "interval_kind"]
    list_display_links = ["date"]
    list_filter = ["model", "scenario", "interval_kind"]
    date_hierarchy = "date"


@admin.register(models.PredictionData)
class PredictionDataAdmin(admin.ModelAdmin):
    list_display = ["date", "prediction", "hospitalized", "icu", "deceased", "deceasedToDate"]
    list_display_links = ["date"]

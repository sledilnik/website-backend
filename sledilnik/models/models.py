import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from sledilnik.easymde.models import MarkdownField


class Person(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"), unique=True)

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")
        ordering = ["name"]

    def __str__(self):
        return self.name


class Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField(_("Password"), max_length=100, help_text=_("Used to authenticate against the API. Hashed form."))
    active = models.BooleanField(_("Active"), default=True)
    name = models.CharField(_("Name"), max_length=100, unique=True)
    www = models.URLField(_("Home page"), null=True, blank=True)
    description = MarkdownField(_("Description"), null=True, blank=True)
    contacts = models.ManyToManyField(Person, verbose_name=_("Contacts"))

    class Meta:
        verbose_name = _("Model")
        verbose_name_plural = _("Models")
        ordering = ["name"]

    def __str__(self):
        return self.name


class Scenario(models.Model):
    name = models.CharField(_("Name"), max_length=100, unique=True)
    description = MarkdownField(_("Description"), null=True, blank=True)

    class Meta:
        verbose_name = _("Modelling scenario")
        verbose_name_plural = _("Modelling scenarios")
        ordering = ["name"]

    def __str__(self):
        return self.name


class PredictionIntervalType(models.Model):
    name = models.CharField(_("Name"), max_length=100, unique=True)
    description = MarkdownField(_("Description"), null=True, blank=True)

    class Meta:
        verbose_name = _("Prediction interval type")
        verbose_name_plural = _("Prediction interval types")
        ordering = ["name"]

    def __str__(self):
        return self.name


class PredictionIntervalWidth(models.Model):
    width = models.PositiveIntegerField(_("Width"), unique=True)

    class Meta:
        verbose_name = _("Prediction interval width")
        verbose_name_plural = _("Prediction interval widths")
        ordering = ["width"]

    def __str__(self):
        return self.width


class Prediction(models.Model):
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)

    date = models.DateField(_("Date"))
    model = models.ForeignKey(Model, on_delete=models.PROTECT, verbose_name=_("Model"))
    scenario = models.ForeignKey(Scenario, on_delete=models.PROTECT, verbose_name=_("Scenario"))
    interval_type = models.ForeignKey(PredictionIntervalType, on_delete=models.PROTECT, verbose_name=_("Interval type"), null=True, blank=True)
    interval_width = models.ForeignKey(PredictionIntervalWidth, on_delete=models.PROTECT, verbose_name=_("Interval width"), null=True, blank=True)

    class Meta:
        verbose_name = _("Prediction")
        verbose_name_plural = _("Predictions")
        unique_together = [("date", "model")]
        ordering = ["-date", "model__name"]

    def __str__(self):
        return "{} @ {}".format(self.model.name, self.date)


class PredictionData(models.Model):
    date = models.PositiveIntegerField(_("Date"))
    prediction = models.ForeignKey(Prediction, on_delete=models.PROTECT, verbose_name=_("Prediction"))

    icu = models.PositiveIntegerField(_("ICU"))
    icuLowerBound = models.PositiveIntegerField(_("ICU lower bound"), null=True, blank=True)
    icuUpperBound = models.PositiveIntegerField(_("ICU upper bound"), null=True, blank=True)

    hospitalized = models.PositiveIntegerField(_("Hospitalized"))
    hospitalizedLowerBound = models.PositiveIntegerField(_("Hospitalized lower bound"), null=True, blank=True)
    hospitalizedUpperBound = models.PositiveIntegerField(_("Hospitalized upper bound"), null=True, blank=True)

    deceased = models.PositiveIntegerField(_("Deceased"))
    deceasedLowerBound = models.PositiveIntegerField(_("Deceased lower bound"), null=True, blank=True)
    deceasedUpperBound = models.PositiveIntegerField(_("Deceased upper bound"), null=True, blank=True)

    deceasedToDate = models.PositiveIntegerField(_("DeceasedToDate"))
    deceasedToDateLowerBound = models.PositiveIntegerField(_("Deceased todate lower bound"), null=True, blank=True)
    deceasedToDateUpperBound = models.PositiveIntegerField(_("Deceased todate upper bound"), null=True, blank=True)

    class Meta:
        verbose_name = _("Prediction data")
        verbose_name_plural = _("Prediction data")
        unique_together = [("prediction", "date")]
        ordering = ["-date", "prediction"]

    def __str__(self):
        return "{} @ {}".format(self.prediction, self.date)

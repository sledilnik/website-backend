from django.db import models
from django.utils.translation import gettext_lazy as _
from sledilnik.easymde.models import MarkdownField

# class Region(models.Model):
#     RED = 'RED'
#     ORANGE = 'ORANGE'
#     GREEN = 'GREEN'
#     STATUS_CHOICES = [
#         (RED, _('Red')),
#         (ORANGE, _('Orange')),
#         (GREEN, _('Green')),
#     ]

#     title = models.CharField(max_length=255, blank=False, null=False, unique=True)
#     status = models.CharField(max_length=255, choices=STATUS_CHOICES, blank=True, null=True)

# Create your models here.
class Restriction(models.Model):
    title = models.CharField(_("Title"), max_length=255, blank=False, null=False)
    rule = MarkdownField(_("Rule"), blank=False, null=False)
    regions = models.CharField(_("Regions"), max_length=255, null=False, blank=False)
    exceptions = MarkdownField(_("Rule exceptions"), blank=True, null=False)
    extra_rules = MarkdownField(_("Extra rules"), blank=True, null=False)
    valid_since = models.DateField(_("Valid since"), blank=True, null=True)
    valid_until = models.DateField(_("Valid until"), blank=True, null=True)
    validity_comment = MarkdownField(_("Validity comment"), blank=True, null=False)
    comments = MarkdownField(_("Comments"), blank=True, null=False)
    legal_link = models.URLField(_("Legal link"), blank=True, null=True)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)
    published = models.BooleanField(_("Published"), default=False)

    order = models.PositiveIntegerField(_("Order"), default=0, null=False, blank=False)

    class Meta(object):
        ordering = ["order"]

    def __str__(self):
        return self.title
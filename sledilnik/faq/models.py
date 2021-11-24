from django.db import models
from django.utils.translation import gettext_lazy as _
from sledilnik.easymde.models import MarkdownField


class Project(models.Model):
    name = models.CharField(_("Name"), max_length=100, unique=True)
    slug = models.SlugField(_("Slug"), max_length=100, unique=True, help_text="Used to query the API")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Faq(models.Model):
    project = models.ForeignKey(Project, verbose_name=_("Project"), on_delete=models.CASCADE)
    position = models.PositiveIntegerField(_("Position"), default=0, null=False, blank=False)

    question = models.CharField(_("Question"), max_length=500)
    answer = MarkdownField(_("Answer"))

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return self.question

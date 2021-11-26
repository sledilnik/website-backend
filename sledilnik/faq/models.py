from django.db import models
from django.utils.translation import gettext_lazy as _
from sledilnik.easymde.models import MarkdownField


class Project(models.Model):
    name = models.CharField(_("Name"), max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Faq(models.Model):
    project = models.ForeignKey(Project, verbose_name=_("Project"), on_delete=models.CASCADE, related_name="faqs")
    position = models.PositiveIntegerField(_("Position"), default=0, null=False, blank=False)

    slug = models.SlugField(_("Slug"), max_length=100, help_text=_('Used to reference the question with a hash link, e.g. https://sledilnik.org/faq#slug'))
    question = models.CharField(_("Question"), max_length=500)
    answer = MarkdownField(_("Answer"))

    class Meta:
        ordering = ["position"]
        constraints = [
            models.UniqueConstraint(fields=["project", "slug"], name="unique_faq_slug_per_project"),
            models.UniqueConstraint(fields=["project", "question"], name="unique_faq_question_per_project"),
        ]

    def __str__(self):
        return self.question


class GlossaryTerm(models.Model):
    project = models.ForeignKey(Project, verbose_name=_("Project"), on_delete=models.CASCADE, related_name="glossary")
    position = models.PositiveIntegerField(_("Position"), default=0, null=False, blank=False)

    slug = models.SlugField(_("Slug"), max_length=100, help_text=_('Used to reference the glossary term in the FAQ text: &lt;span data-term=&quot;slug&quot;&gt;some term&lt;/span&gt;'))
    term = models.CharField(_("Term"), max_length=100)
    definition = MarkdownField(_("Definition"))

    class Meta:
        verbose_name = _("Glossary term")
        verbose_name_plural = _("Glossary terms")
        ordering = ["position"]
        constraints = [
            models.UniqueConstraint(fields=["project", "slug"], name="unique_glossary_slug_per_project"),
            models.UniqueConstraint(fields=["project", "term"], name="unique_glossary_term_per_project"),
        ]

    def __str__(self):
        return self.term

from django.db import models
from django.utils.translation import gettext_lazy as _

from sledilnik.easymde.models import MarkdownField


class Post(models.Model):
    created = models.DateTimeField(_("Created"), db_index=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)

    published = models.BooleanField(
        _("Published"), default=False, db_index=True)
    pinned = models.BooleanField(_("Pinned"), default=False, db_index=True)

    title = models.CharField(_("Title"), max_length=200)
    link_to = models.URLField(_("Link to"), null=True, blank=True)
    image = models.ImageField(
        _("Image"), upload_to="posts/%Y/%m/%d/%H/%M/%S", null=True, blank=True)
    image_caption = models.CharField(
        _("Image caption"), max_length=200, null=True, blank=True)
    author = models.CharField(
        _("Author"), max_length=100, null=True, blank=True)
    blurb = MarkdownField(_("Blurb"))
    body = MarkdownField(_("Body"), null=True, blank=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["-pinned", "-created", "title"]

    def __str__(self):
        return self.title

from django.db import models
from django.utils.translation import gettext_lazy as _

from sledilnik.tinymce import HTMLField


class Post(models.Model):
    published = models.BooleanField(_("Published"), default=False)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)

    author = models.CharField(_("Author"), max_length=100, null=True, blank=True)
    image = models.ImageField(_("Image"), upload_to="posts/%Y/%m/%d/%H/%M/%S", null=True, blank=True)
    title = models.CharField(_("Title"), max_length=200)
    blurb = HTMLField(_("Blurb"), options={"toolbar": "undo redo | bold italic subscript superscript | removeformat"})
    link_to = models.URLField(_("Link to"), null=True, blank=True)
    body = HTMLField(_("Body"), null=True, blank=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ["-created", "title"]

    def __str__(self):
        return self.title

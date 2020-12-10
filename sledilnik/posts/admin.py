from django import forms
from django.contrib import admin

from sledilnik.utils import TranslationAdmin
from sledilnik.easymde.widgets import MarkdownWidget

from . import models


simpleMarkdownWidget = MarkdownWidget(options={
    "toolbar": ["bold", "italic", "|", "preview", "|", "guide"]
})


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        widgets = {
            'blurb_sl': simpleMarkdownWidget,
            'blurb_en': simpleMarkdownWidget,
        }
        fields = '__all__'


@admin.register(models.Post)
class Post(TranslationAdmin):
    form = PostForm
    list_display = ["published", "title", "created", "updated"]
    list_display_links = ["title"]
    date_hiearchy = "created"
    search_fields = ["author", "title", "blurb", "body"]

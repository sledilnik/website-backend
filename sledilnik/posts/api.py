from tastypie.resources import ModelResource

from django.conf import settings
from django.utils import translation

from .models import Post


class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.filter(published=True)
        resource_name = "posts"
        fields = ["created", "updated", "author", "title", "image", "blurb", "link_to"]

    def dehydrate(self, bundle):
        lang = bundle.request.GET.get("lang")
        if lang not in [lng[0] for lng in settings.LANGUAGES]:
            lang = settings.LANGUAGE_CODE
        translation.activate(lang)

        return bundle

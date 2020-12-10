import datetime

from tastypie.resources import ModelResource

from django.conf import settings
from django.utils import translation

from .models import Post


class PostResource(ModelResource):
    class Meta:
        resource_name = "posts"
        queryset = Post.objects.all()
        fields = ["id", "created", "updated", "author", "title", "image", "blurb", "link_to", "body"]

    def get_object_list(self, request):
        return super().get_object_list(request).filter(published=True, created__lte=datetime.datetime.now())

    def dehydrate(self, bundle):
        lang = bundle.request.GET.get("lang")

        if lang not in [lng[0] for lng in settings.LANGUAGES]:
            lang = settings.LANGUAGE_CODE
        translation.activate(lang)

        if bundle.obj.image:
            bundle.data["image"] = bundle.request.build_absolute_uri(bundle.obj.image.url)

        return bundle

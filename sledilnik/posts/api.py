from django.utils import timezone

from tastypie.resources import ModelResource
from tastypie.cache import SimpleCache
from sorl.thumbnail import get_thumbnail

from django.conf import settings
from django.utils import translation

from .models import Post


class PostResource(ModelResource):
    class Meta:
        resource_name = "posts"
        queryset = Post.objects.all()
        fields = ["id", "created", "updated", "author", "title",
                  "image", "image_caption", "blurb", "link_to", "body"]
        cache = SimpleCache(timeout=60, public=True)

    def get_object_list(self, request):
        kwargs = {
            "published": True,
            "created__lte": timezone.now()
        }
        if request.GET.get("page") == "home":
            kwargs["on_homepage"] = True
        return super().get_object_list(request).filter(**kwargs).order_by('-pinned', '-created')

    def dehydrate(self, bundle):
        lang = bundle.request.GET.get("lang")

        if lang not in [lng[0] for lng in settings.LANGUAGES]:
            lang = settings.LANGUAGE_CODE
        translation.activate(lang)

        if bundle.obj.image:
            bundle.data["image"] = bundle.request.build_absolute_uri(
                get_thumbnail(bundle.obj.image, "800x810").url)
            bundle.data["image_thumb"] = bundle.request.build_absolute_uri(
                get_thumbnail(bundle.obj.image, "400x405").url)

        return bundle

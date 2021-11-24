from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.cache import SimpleCache

from django.conf import settings
from django.utils import translation

from .models import Project, Faq


class FaqResource(ModelResource):
    class Meta:
        queryset = Faq.objects.all()
        fields = ["position", "question", "answer"]
        cache = SimpleCache(timeout=60, public=True)

    def dehydrate(self, bundle):
        del(bundle.data["resource_uri"])

        return bundle


class FaqProjectResource(ModelResource):
    faq = fields.ToManyField(FaqResource, "faqs", full=True, use_in="detail")

    class Meta:
        resource_name = "faq"
        queryset = Project.objects.all()
        fields = ["id", "name"]
        allowed_methods = ["get"]
        cache = SimpleCache(timeout=60, public=True)

    def dehydrate(self, bundle):
        lang = bundle.request.GET.get("lang")
        if lang not in [lng[0] for lng in settings.LANGUAGES]:
            lang = settings.LANGUAGE_CODE
        translation.activate(lang)

        return bundle

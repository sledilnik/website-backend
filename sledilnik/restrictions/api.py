from tastypie.resources import ModelResource
from tastypie.cache import SimpleCache

from django.conf import settings
from django.utils import translation
from django.db.models import Max

from .models import Restriction


class RestrictionResource(ModelResource):
    class Meta:
        resource_name = "restrictions"
        queryset = Restriction.objects.all()
        fields = ["id", "title", "rule", "regions", "exceptions", "extra_rules",
                  "valid_since", "valid_until", "validity_comment", "comments", "legal_link", "order"]
        cache = SimpleCache(timeout=60, public=True)

    def get_object_list(self, request):
        return super().get_object_list(request).filter(published=True).order_by("order")

    def alter_list_data_to_serialize(self, request, data):
        data['meta']['last_update'] = self.get_object_list(request).aggregate(Max("updated")).get('updated__max')
        return data

    def dehydrate(self, bundle):
        lang = bundle.request.GET.get("lang")

        if lang not in [lng[0] for lng in settings.LANGUAGES]:
            lang = settings.LANGUAGE_CODE
        translation.activate(lang)

        return bundle

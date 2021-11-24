from tastypie.api import Api

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _

import sledilnik.modeling.urls

from sledilnik.posts.api import PostResource
from sledilnik.restrictions.api import RestrictionResource
from sledilnik.faq.api import FaqProjectResource

admin.site.enable_nav_sidebar = False
admin.site.site_header = _("Sledilnik Administration")
admin.site.site_title = _("Sledilnik Administration")
admin.site.index_title = _("Site administration")

api = Api(api_name='v1')
api.register(PostResource())
api.register(RestrictionResource())
api.register(FaqProjectResource())

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/modeling/', include(sledilnik.modeling.urls)),
    path('api/', include(api.urls)),
]

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns

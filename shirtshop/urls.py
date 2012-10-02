from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^home/$','shirtshop.shirts.views.home'),
    (r'^shirtshop/shirts/views/get_shirt_info/','shirtshop.shirts.views.get_shirt_info'),
    (r'^about/$','shirtshop.shirts.views.about'),
    (r'^blog/$','http://www.google.com')

)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^home/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/Sam/Code/shirtshop/shirtshop/static/'}),
    )

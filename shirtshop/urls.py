from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
    (r'^home/$','shirtshop.shirts.views.home'),
    (r'^about/$','shirtshop.shirts.views.about'),
    (r'^blog/$','http://www.google.com'),
    (r'^patterns/$','shirtshop.shirts.views.patterns'),

)



from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^TextAnalysis/', include('TextAnalysis.foo.urls')),
    url('^', include('globocore.delivery_urls')),

    url('^', include('globocore.urls')),

    url('^', include('textAnalysis.urls')),


    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # (r'^m/(?P<path>.*)$', 'django.views.static.serve', {
    #     'document_root': settings.MEDIA_ROOT,
    # }),

        
    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

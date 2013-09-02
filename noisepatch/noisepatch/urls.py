from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'noisepatch.views.home', name='home'),
    # url(r'^noisepatch/', include('noisepatch.foo.urls')),
    
    (r'^todo/', include('todo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

from wiki.urls import get_pattern as get_wiki_pattern
from django_notify.urls import get_pattern as get_notify_pattern
urlpatterns += patterns('',
    (r'^notify/', get_notify_pattern()),
    (r'^wiki/', get_wiki_pattern())
)

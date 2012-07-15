from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miniblog.views.home', name='home'),
    # url(r'^miniblog/', include('miniblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # URLs for blog engine app.
    url(r'^$', 'blogengine.views.index', name='index'),
    url(r'^article/(?P<article_id>\d+)/$', 'blogengine.views.article', name='article'),
    url(r'^archive/(?P<year>\d+)/(?P<month>\d+)/$', 'blogengine.views.archive', name='archive'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

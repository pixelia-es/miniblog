from django.conf.urls import patterns, url

urlpatterns = patterns('blogengine.views',
    # URLs for blog engine app.
    url(r'^$', 'index', name='index'),
    url(r'^article/(?P<article_id>\d+)/$', 'article', name='article'),
    url(r'^archive/(?P<year>\d+)/(?P<month>\d+)/$', 'archive', name='archive'),
)

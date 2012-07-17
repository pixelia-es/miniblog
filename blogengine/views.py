#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Views for the blog engine app."""

from blogengine.models import Article

from django.conf import settings
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

import datetime


def index(request):
    """Shows the first 10 articles if they exists."""
    latest_articles = Article.objects.all().order_by('-creation_time')[:10]
    now = datetime.datetime.now()
    return render_to_response('blogengine/index.html',
                              {'articles': latest_articles,
                               'year': now.year,
                               'month': now.month,
                               # TODO: This can be DRYer with a custom Context,
                               # although for this example seemed overkilling.
                               'ANALYTICS_ID': settings.ANALYTICS_ID},
                              context_instance=RequestContext(request))


def article(request, article_id):
    """Shows the article in a single page for detailed view."""
    article = get_object_or_404(Article, pk=article_id)
    return render_to_response('blogengine/article.html',
                              {'article': article,
                               # TODO: This can be DRYer with a custom Context,
                               # although for this example seemed overkilling.
                               'ANALYTICS_ID': settings.ANALYTICS_ID},
                              context_instance=RequestContext(request))


def archive(request, year, month):
    """Looks for articles in the specified month."""
    start_time = datetime.datetime(year=int(year),
                                   month=int(month),
                                   day=1)
    # This conversion for the time range is needed since App Engine
    # does not support __month queries (but __year is supported).
    # Substracting 1 millisecond yields the best resoultion. Time
    # zone is not supported (Django will store UTC times).
    end_time = (datetime.datetime(year=int(year),
                                 month=int(month) + 1,
                                 day=1) -
                datetime.timedelta(milliseconds=1))
    articles = Article.objects.filter(creation_time__gte=start_time,
                                      creation_time__lte=end_time)
    return render_to_response('blogengine/archive.html',
                              {'year': year,
                               'month': month,
                               'articles': articles,
                               # TODO: This can be DRYer with a custom Context,
                               # although for this example seemed overkilling.
                               'ANALYTICS_ID': settings.ANALYTICS_ID},
                              context_instance=RequestContext(request))

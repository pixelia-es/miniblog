#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Views for the blog engine app."""

from blogengine.models import Article
from django.conf import settings
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext


def index(request):
    """Shows the first 10 articles if they exists."""
    latest_articles = Article.objects.all().order_by('-creation_time')[:10]
    return render_to_response('blogengine/index.html',
                              {'articles': latest_articles,
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
    articles = Article.objects.filter(creation_time__year=year,
                                      creation_time__month=month)
    return render_to_response('blogengine/archive.html',
                              {'year': year,
                               'month': month,
                               'articles': articles,
                               # TODO: This can be DRYer with a custom Context,
                               # although for this example seemed overkilling.
                               'ANALYTICS_ID': settings.ANALYTICS_ID},
                              context_instance=RequestContext(request))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Models module for the blog engine app."""

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """Category model that allows classify the articles."""
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    """Article model that stores the text and its metadata."""
    title = models.CharField(max_length=500)
    text = models.TextField()
    author = models.ForeignKey(User)
    creation_time = models.DateTimeField()
    last_update_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return '"%s" by %s' % (self.title, self.author.username)

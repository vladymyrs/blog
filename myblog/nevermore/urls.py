__author__ = 'vsaienko'
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.BlogIndex.as_view(), name="index")
)
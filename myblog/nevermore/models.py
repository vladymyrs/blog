from django.db import models
from django_markdown.models import MarkdownField


class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __unicode__(self):
        return self.slug


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
    title = models.CharField(max_length=255, unique=True)
    body = MarkdownField()
    slug = models.SlugField(max_length=255, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateField(db_index=True, auto_now_add=True)
    modified = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    object = EntryQuerySet.as_manager()

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]


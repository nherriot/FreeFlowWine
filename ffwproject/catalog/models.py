from __future__ import unicode_literals

from django.db import models

# The category model is used to store products. This helps us categorise the different products and then easily display
# those products which will be in a certain category help within the category model


class Category(models.Model):
    name        = models.CharField(max_length=50)
    slug        = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
    description = models.TextField()
    is_active   = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords", max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_descriptions = models.CharField("Meta Descriptions", max_length=255, help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), {'category_slug': self.slug})

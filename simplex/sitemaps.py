from django.contrib.sitemaps import Sitemap

from theblog.models import models


class ArticleSitemap(Sitemap):
    name = 'video'
    changefreq = 'daily'
    limit = 50000

    def items(self):
        return models.Post.objects.order_by('id')

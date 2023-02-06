from django.contrib.sitemaps import Sitemap

from theblog.models import Post


class ArticleSitemap(Sitemap):
    name = 'post'
    changefreq = "hourly"
    priority = 1.0
    limit = 50000
   

    def items(self):
        return Post.objects.all().order_by('-id')
    def location(self,obj):
        return '/%s' % (obj.slug)
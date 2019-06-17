from django.contrib.sitemaps import Sitemap
from .models import Post
from django.urls import reverse

class PostSitemap(Sitemap):

    def items(self):
        return Post.objects.all()


    def lastmod(self, obj):
        return obj.pup_date


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['about_as', 'mix_part', 'computer_part', 'offer_part', 'mobile_part', 'post']


    def location(self, item):
        return reverse(item)

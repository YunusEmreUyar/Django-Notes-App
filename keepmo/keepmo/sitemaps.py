from django.contrib.sitemaps import Sitemap
from notes.models import NoteBook
from django.urls import reverse
 
class NoteBookSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return NoteBook.objects.all()

    def location(self,obj):
        return f'/notebook/{obj.id}'


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)
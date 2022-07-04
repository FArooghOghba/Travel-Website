from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils import timezone
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "Blog newest post"
    link = "rss/feed"
    description = "Best blog ever."

    def items(self):
        return Post.objects.filter(publish_date__lte=timezone.now(), status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]

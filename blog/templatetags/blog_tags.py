from django import template
from django.utils import timezone
from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts():
    posts = Post.objects.filter(publish_date__lte=timezone.now(), status=True)[:4]
    return {'posts': posts}

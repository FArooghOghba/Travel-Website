from django import template
from django.utils import timezone

from blog.models import Post

register = template.Library()


@register.inclusion_tag('website/website-blog-area.html')
def blog_area():
    all_post = Post.objects.filter(publish_date__lte=timezone.now(), status=True)[:6]
    return {'all_post': all_post}

from blog.models import *

from django import template
from django.utils import timezone
from django.db.models.aggregates import Count

register = template.Library()


@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts():
    posts = Post.objects.filter(publish_date__lte=timezone.now(), status=True)[:4]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-category.html')
def post_categories():
    # result = Category.objects.annotate(post_count=Count('post'))
    # for cat in result:
    #     print(cat, cat.post_count)

    categories = Category.objects.all()
    posts = Post.objects.filter(publish_date__lte=timezone.now(), status=True)

    post_categories_count = {}
    for category in categories:
        post_categories_count[category.name] = posts.filter(category=category).count()

    return {'post_cats_count': post_categories_count}

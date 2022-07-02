from django import template
from django.db.models import Count
from django.utils import timezone

from blog.models import *

register = template.Library()


@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts():
    posts = Post.objects.filter(publish_date__lte=timezone.now(), status=True)[:4]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-post-category.html')
def post_categories():
    # filter categories count with django ORM
    cat_post_count = Category.objects. \
        filter(post__publish_date__lte=timezone.now(), post__status=True). \
        annotate(post_count=Count('post'))

    return {'cat_post_count': cat_post_count}

    # categories = Category.objects.all()
    # posts = Post.objects.filter(publish_date__lte=timezone.now(), status=True)
    #
    # post_categories_count = {}
    # for category in categories:
    #     post_categories_count[category.name] = posts.filter(category=category).count()
    #
    # return {'post_cats_count': post_categories_count}

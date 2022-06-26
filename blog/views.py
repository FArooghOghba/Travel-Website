from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post


# Create your views here.

def blog_home_view(request):
    all_post = Post.objects.filter(publish_date__lte=timezone.now(), status=True)

    context = {'all_post': all_post}
    return render(request, template_name='blog/blog-home.html', context=context)


def blog_single_view(request, post_id):
    current_post = get_object_or_404(Post, pk=post_id, publish_date__lte=timezone.now(), status=True)
    current_post.counted_views += 1
    current_post.save()

    # prev_post = Post.objects.filter(             # find prev & next page with django orm.
    #     publish_date__lte=timezone.now(),
    #     status=True,
    #     publish_date__lt=current_post.publish_date,
    # ).first()
    # next_post = Post.objects.filter(
    #     publish_date__lte=timezone.now(),
    #     status=True,
    #     publish_date__gt=current_post.publish_date
    # ).first()

    # find prev & next page with list comprehension.
    all_post = Post.objects.filter(publish_date__lte=timezone.now(), status=True)
    prev_post = [post for post in all_post if post.publish_date < current_post.publish_date]
    next_post = [post for post in list(reversed(all_post)) if post.publish_date > current_post.publish_date]

    context = {
        'current_post': current_post,
        'next_post': next_post,
        'prev_post': prev_post
    }
    return render(request, template_name='blog/blog-single.html', context=context)

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator

from blog.models import Post


# Create your views here.

def blog_home_view(request):
    all_post = Post.objects.filter(publish_date__lte=timezone.now(), status=True)

    context = {'all_post': all_post}
    return render(request, template_name='blog/blog-home.html', context=context)


def blog_single_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id, publish_date__lte=timezone.now(), status=True)
    post.counted_views += 1
    post.save()

    context = {'post': post}
    return render(request, template_name='blog/blog-single.html', context=context)

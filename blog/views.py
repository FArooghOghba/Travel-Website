from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from blog.models import Post, Comment
from blog.forms import CommentForm


# Create your views here.

def blog_home_view(request, **kwargs):
    all_post = Post.objects.filter(publish_date__lte=timezone.now(), status=True)
    if kwargs.get('cat_name') is not None:
        all_post = all_post.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') is not None:
        all_post = all_post.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') is not None:
        all_post = all_post.filter(tags__name=kwargs['tag_name'])

    paginator = Paginator(all_post, 3)
    try:
        page_number = request.GET.get('page')
        all_post_pages = paginator.get_page(page_number)
    except PageNotAnInteger:
        all_post_pages = paginator.get_page(1)
    except EmptyPage:
        all_post_pages = paginator.get_page(1)

    context = {'all_post_pages': all_post_pages}
    return render(request, template_name='blog/blog-home.html', context=context)


def blog_single_view(request, post_id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, 'Your comment submitted Successfully.')
        else:
            messages.error(request, "Your comment didn't submitted.")

    current_post = get_object_or_404(Post, pk=post_id, publish_date__lte=timezone.now(), status=True)
    if not current_post.login_require or (current_post.login_require is True and request.user.is_authenticated is True):
        current_post.counted_views += 1
        current_post.save()

        all_post = Post.objects.filter(publish_date__lte=timezone.now(), status=True)
        prev_post = [post for post in all_post if post.publish_date < current_post.publish_date]
        next_post = [post for post in list(reversed(all_post)) if post.publish_date > current_post.publish_date]

        comments = Comment.objects.filter(post=current_post, approved=True)

        # prev_post = Post.objects.filter(             # find prev & next page with django orm.
        #     publish_date__lte=timezone.now(),
        #     status=True,
        #     publish_date__lt=current_post.publish_date,
        # )
        # next_post = Post.objects.filter(
        #     publish_date__lte=timezone.now(),
        #     status=True,
        #     publish_date__gt=current_post.publish_date
        # )

        # find prev & next page with list comprehension.

        context = {
            'current_post': current_post,
            'comments': comments,
            'next_post': next_post,
            'prev_post': prev_post
        }
        return render(request, template_name='blog/blog-single.html', context=context)
    else:
        return redirect('accounts:login')


def blog_search_view(request):
    search_post = Post.objects.filter(publish_date__lte=timezone.now(), status=True)

    if request.method == 'GET':
        if s := request.GET.get('s'):
            search_post = search_post.filter(content__contains=s)

    context = {'all_post': search_post}
    return render(request, 'blog/blog-home.html', context=context)

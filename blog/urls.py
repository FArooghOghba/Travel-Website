from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_home_view, name='home'),
    path('single/<int:post_id>/', blog_single_view, name='single'),

    path('category/<str:cat_name>/', blog_home_view, name='category'),
    path('tag/<str:tag_name>/', blog_home_view, name='tags'),
    path('author/<str:author_username>/', blog_home_view, name='author'),
    path('search/', blog_search_view, name='search'),
]

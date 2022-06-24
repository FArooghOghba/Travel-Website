from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_home_view, name='home'),
    path('single/<int:post_id>/', blog_single_view, name='single')
]

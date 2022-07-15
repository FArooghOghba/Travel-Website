from django.shortcuts import reverse, redirect
from django.conf import settings


class ComingSoonModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.META.get('PATH_INFO', "")

        if settings.COMING_SOON_MODE and path != reverse('website:coming_soon'):
            response = redirect(reverse('website:coming_soon'))
            return response

        response = self.get_response(request)

        return response

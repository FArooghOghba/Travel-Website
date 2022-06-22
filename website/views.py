from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request, template_name='website/index.html')


def about_view(request):
    return render(request, template_name='website/about.html')


def contact_view(request):
    return render(request, template_name='website/contact.html')


def elements_view(request):
    return render(request, template_name='website/elements.html')

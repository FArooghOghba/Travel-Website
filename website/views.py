from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm, NewsletterForm


# Create your views here.
def index_view(request):
    return render(request, template_name='website/index.html')


def about_view(request):
    return render(request, template_name='website/about.html')


def contact_view(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your ticket submitted Successfully.')
        else:
            messages.error(request, "Your ticket didn't submitted.")

    contact_form = ContactForm()
    context = {'contact_form': contact_form}
    return render(request, template_name='website/contact.html', context=context)


def elements_view(request):
    return render(request, template_name='website/elements.html')


def newsletter_view(request):
    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()

    return HttpResponseRedirect('/')

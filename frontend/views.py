import requests
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from settings.api import get_setting
from . import models
from . import forms


class IndexView(ListView):
    template_name = 'frontend/index.html'
    context_object_name = 'front_item'
    queryset = models.FrontItem.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = models.NewsItem.objects.filter(publish__exact=True).filter(date__lte=timezone.now())[:3]
        return context


class SentView(TemplateView):
    template_name = 'frontend/sent.html'


def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            data = {
                'content': "{} <{}> has left a message\n\n{}".format(
                    form.cleaned_data['name'],
                    form.cleaned_data['email'],
                    form.cleaned_data['message']
                )
            }
            r = requests.post(get_setting('skynet_message_url'), data=data)
            return HttpResponseRedirect(reverse('pages:sent'))
    else:
        form = forms.ContactForm()

    return render(request, 'frontend/contact.html', {'form': form})

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from settings.api import create_or_update_setting
from . import forms


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'


def settings(request):
    if request.method == 'POST':
        form = forms.SettingForm(request.POST)
        if form.is_valid():
            key = form.cleaned_data['key']
            value = eval(form.cleaned_data['value'])
            create_or_update_setting(key, value)
            messages.success(request, '<strong>{}</strong> successfully updated.'.format(form.cleaned_data['key']))
            return HttpResponseRedirect(reverse('dashboard:settings'))
    else:
        form = forms.SettingForm()

    return render(request, 'dashboard/settings.html', {'form': form})

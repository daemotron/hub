from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from settings.api import create_or_update_setting
from . import forms


def staff_check(user):
    return user.is_staff


class IndexView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard/home.html'

    def test_func(self):
        return staff_check(self.request.user)


@login_required
@user_passes_test(staff_check)
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

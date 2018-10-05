import requests
from django.contrib import messages
from django.contrib.auth import logout, login, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render

from fse.payment import issue_payment
from settings.api import get_setting
from fse.account import get_account_id
from banner.models import UserStat
from . import models
from . import forms


class IndexView(ListView):
    template_name = 'frontend/index.html'
    context_object_name = 'front_item'
    queryset = models.FrontItem.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = models.NewsItem.objects.filter(publish__exact=True).filter(date__lte=timezone.now())[:3]
        try:
            context['greet'] = models.ContentSnippet.objects.get(cid__exact='front_greet')
        except models.ContentSnippet.DoesNotExist:
            context['greet'] = None
        return context


class SentView(TemplateView):
    template_name = 'frontend/sent.html'


class PrivacyView(TemplateView):
    template_name = 'frontend/privacy.html'


class LegalView(TemplateView):
    template_name = 'frontend/legal.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'frontend/profile.html'


@login_required
def logout_view(request, target=None):
    logout(request)
    target = request.GET.get('target', None)
    if not target or target == '/profile/':
        target = reverse('index:index')
    return HttpResponseRedirect(target)


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
            return HttpResponseRedirect(reverse('contact:sent'))
    else:
        form = forms.ContactForm()

    return render(request, 'frontend/contact.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password']
            )
            user_profile = models.Profile(
                user=user,
                fseid=get_account_id(form.cleaned_data['username'])
            )
            user_profile.save()
            user_stat = UserStat(user=user)
            user_stat.save()
            login(request, user)
            issue_payment(get_setting('profile_validation_payment_sender'), user.username, 0.01, user_profile.token)
            return HttpResponseRedirect(reverse('profile:index'))
    else:
        form = forms.RegisterForm()
    return render(request, 'frontend/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            user.email = form.cleaned_data['email']
            user.save()
            user_profile = user.profile
            user_profile.avatar = form.cleaned_data['avatar']
            user_profile.save()
            if form.cleaned_data['token'] and not user_profile.valid:
                if form.cleaned_data['token'] == user_profile.token:
                    user_profile.valid = True
                    user_profile.validated = timezone.now()
                    user_profile.save()
                    messages.success(request, 'Account has been validated.')
                else:
                    form.add_error('token', 'The token specified is not valid for this account.')
            if form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password has been updated.')
            messages.success(request, 'Settings have been updated.')
            return HttpResponseRedirect(reverse('profile:index'))
    else:
        form = forms.ProfileForm(initial={'email': request.user.email, 'avatar': request.user.profile.avatar})
    return render(request, 'frontend/profile.html', {'form': form})

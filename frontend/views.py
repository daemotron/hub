from django.utils import timezone
from django.views.generic import ListView
from . import models


class IndexView(ListView):
    template_name = 'frontend/index.html'
    context_object_name = 'front_item'
    queryset = models.FrontItem.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = models.NewsItem.objects.filter(publish__exact=True).filter(date__lte=timezone.now())[:3]
        return context

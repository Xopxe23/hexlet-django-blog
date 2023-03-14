from django.shortcuts import render
from django.views.generic.base import TemplateView


def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(request, 'about.html', {'tags': tags})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import View


def index(request, tags, article_id):
    return HttpResponse(f'Article №{article_id}. Tag {tags}')


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse('article_info', kwargs={'tags': 'python', 'article_id': 42}))

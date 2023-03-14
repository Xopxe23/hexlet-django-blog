from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from .models import Article


def index(request, tags, article_id):
    return HttpResponse(f'Article №{article_id}. Tag {tags}')


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            'article/index.html',
            context={'articles': articles, }
        )

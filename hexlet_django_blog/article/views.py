from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from .models import Article
from .forms import ArticleForm
from django.contrib import messages


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


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'article/show.html',
            context={'article': article}
        )


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article has been created!')
            return redirect('articles')
        return render(request, 'article/create.html', {'form': form})

from django.shortcuts import render


def index(request):
    context = {
        "title": "Article",
        "app_name": "App Article"
    }
    return render(
        request,
        'article/index.html',
        context=context
    )

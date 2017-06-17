from django.http import HttpResponse
from django.shortcuts import render
from .training import TrainClassify


def view(request):

    url = request.GET.get('article_url')
    genre = TrainClassify.main()

    d = {
        'genre': genre,
        'article_url': url,
    }
    return render(request, 'article/view.html', d)
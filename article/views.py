from django.http import HttpResponse
from django.shortcuts import render
from .training import TrainClassify
from . import forms


def view(request):
    form = forms.URLForm(request.GET or None)
    if form.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = 'データ検証に失敗しました'

    genre = TrainClassify.main(form)



    d = {
        'genre': genre,
        'form': form,
    }
    return render(request, 'article/view.html', d)
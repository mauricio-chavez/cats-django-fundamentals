"""Cats app vies"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .forms import CatForm
from .models import Cat


def index(request):
    breed = request.GET.get('breed')
    if not breed:
        cats = Cat.objects.all()
    else:
        cats = Cat.objects.filter(breed=breed)

    return render(
        request,
        'index.html',
        {
            'user': f'@{request.user}',
            'cats': cats,
        }
    )


def create(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            cat = form.save(request)
            messages.success(
                request, f'{cat.name} ha sido creado correctamente'
            )
            return redirect('gatitos')
    else:
        form = CatForm()

    return render(request, 'create.html', {'form': form})

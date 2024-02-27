from django.shortcuts import render

from src.forms import GeeksForm


def home_view(request):
    context = {}
    context['form'] = GeeksForm()
    return render(request, 'home.html', context)

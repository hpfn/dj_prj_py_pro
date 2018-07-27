from django.shortcuts import render


def index(request):
    context = {'moveis': ''}
    return render(request, 'moveis/index.html', context)

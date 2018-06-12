from django.shortcuts import render


def home(request):
    context = {'simple_test': 'Hello Cloudinary'}
    return render(request, 'core/home.html', context)

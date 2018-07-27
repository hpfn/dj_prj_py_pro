from django.urls import path
from certgen.moveis.views import index

app_name = 'moveis'

urlpatterns = [
    path('', index, name='index'),
]

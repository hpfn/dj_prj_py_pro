from django.db.models import Prefetch
from django.shortcuts import render
from django.utils import timezone

from certgen.moveis.models import Categorias, Movel


def index(request):
    qs = Categorias.objects.order_by('titulo').prefetch_related(
        Prefetch(
            'movel_set',
            queryset=Movel.objects.filter(
                ultima_atualizacao__gt='2018-07-31',
            ).order_by('ultima_atualizacao').reverse(),
            to_attr='movel_ultimos'
        ))

    context = {
        'categorias': list(qs),
        #'ultimo': qs.movel_ultimo,
    }
    return render(request, 'moveis/index.html', context)

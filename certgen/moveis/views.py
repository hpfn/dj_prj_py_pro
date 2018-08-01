from datetime import datetime
from django.utils.timezone import make_aware

from django.db.models import Prefetch
from django.shortcuts import render

from certgen.moveis.models import Categorias, Movel


def index(request):
    date_hard_coded = datetime(2018, 7, 31, hour=7, minute=0, second=0)
    qs = Categorias.objects.order_by('titulo').prefetch_related(
        Prefetch(
            'movel_set',
            queryset=Movel.objects.filter(
                ultima_atualizacao__gt=make_aware(date_hard_coded),
            ).order_by('ultima_atualizacao').reverse(),
            to_attr='movel_ultimos'
        ))

    context = {
        'categorias': list(qs),
        # 'ultimo': qs.movel_ultimo,
    }
    return render(request, 'moveis/index.html', context)

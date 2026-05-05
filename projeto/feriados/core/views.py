from django.shortcuts import render
from datetime import datetime
from core.models import FeriadoModel

def feriados(request):
    hoje = datetime.today()
    qs = FeriadoModel.objects.filter(dia=hoje.day)
    qs = qs.filter(mes=hoje.month)
    if len(qs) == 0:
        contexto = {'feriado_name': '','feriado':False}
    else:
        contexto = {'feriado_name': qs[0].nome, 'feriado':True}
    return render(request, 'feriado_template.html', context=contexto)
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


from django.http import JsonResponse
def json_simprao(request):
    feriados = FeriadoModel.objects.all().values('id', 'nome', 'dia', 'mes')
    return JsonResponse(list(feriados), safe=False)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FeriadoSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class FeriadoListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        feriados = FeriadoModel.objects.all()
        serializer = FeriadoSerializer(feriados, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeriadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeriadoDetailView(APIView):
    def get(self, request, pk):
        feriado = get_object_or_404(FeriadoModel, pk=pk)
        serializer = FeriadoSerializer(feriado)
        return Response(serializer.data)

    def put(self, request, pk):
        feriado = get_object_or_404(FeriadoModel, pk=pk)
        serializer = FeriadoSerializer(feriado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        feriado = get_object_or_404(FeriadoModel, pk=pk)
        feriado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
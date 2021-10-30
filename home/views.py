from django.db.models import Q
from django.shortcuts import render, Http404, get_object_or_404
from .models import Pizzaria
from .serializers import PizzariaSerializer
from rest_framework import viewsets

class PizzariaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset=Pizzaria.objects.all()
    serializer_class = PizzariaSerializer   


def index(request):
    dados = Pizzaria.objects.order_by('-id').filter(
        mostrar=True
    )
    return render(request, 'home/index.html', {'dados': dados})


def mostrar(request, idbusca):
    dados = get_object_or_404(Pizzaria, id=idbusca)
    return render(request, 'home/detPizza.html', {'dados': dados})


def buscar(request):
    x = request.GET['buscar']
    if x is None or not x:
        return render(request, 'home/index.html')

    dados = Pizzaria.objects.order_by('titulo').filter(
        Q(titulo__icontains=x) | Q(descricao__icontains=x)
    )
    return render(request, 'home/index.html', {'dados': dados})

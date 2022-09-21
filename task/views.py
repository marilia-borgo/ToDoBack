
from asyncio import tasks
from multiprocessing import context
from turtle import pos
from django.shortcuts import render, get_object_or_404
import requests
import  json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tasks
from django.forms.models import model_to_dict


def listartask(request):
    task = Tasks.objects.all()
    c = []
    for task in task:
        c.append({
            'id': task.id,
            'titulo': task.titulo,
            'projeto': task.projeto,
            'dueTo': task.dueTo,
            'feito': task.feito,
        })
    context = {'tasks': c}
    return JsonResponse(context)

@csrf_exempt
def addtask(request):
    if request.method == 'POST':
        valores = request.body
        task = json.loads(valores.decode('utf-8'))
        Tasks.objects.create(titulo=task.get('titulo'), projeto=task.get('projeto'),
                            dueTo=task.get('dueTo'),feito=task.get('feito'),)
        return JsonResponse({'message': 'sucesso','code': 200})
    else:
        response = {'erro': 'precisa ser Get'}
        return JsonResponse(response)
from .models import Formula
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json


def home(request):
    return render(request, 'home.html')

def create_formula_form(request):
    return render(request, 'create_formula.html')

def list_formulas(request):
    queryset = Formula.objects.all()
    context = list(queryset.values('dose', 'frequency', 'unity', 'medicationId', 'presentation'))
    return JsonResponse(context, safe=False)

def create_formula(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        formula = Formula.objects.create(
            dose=data['dose'],
            frequency=data['frequency'],
            unity=data['unity'],
            medicationId=data['medicationId'],
            presentation=data['presentation']
        )
        formula.save()
        return JsonResponse({'message': 'Formula created successfully!'}, status=201)
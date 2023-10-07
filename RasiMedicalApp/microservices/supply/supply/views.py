from .models import Supply
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def home(request):
    return render(request, 'home.html')

def create_supply_form(request):
    return render(request, 'create_supply.html')

def list_supplies(request):
    queryset = Supply.objects.all()
    context = list(queryset.values('id', 'name', 'description', 'price', 'quantity'))
    return JsonResponse(context, safe=False)

def create_supply(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        supply = Supply.objects.create(
            name=data['name'],
            description=data['description'],
            price=data['price'],
            quantity=data['quantity']
        )
        supply.save()
        return JsonResponse({'message': 'Supply created successfully!'}, status=201)
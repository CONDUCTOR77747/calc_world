# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:17:08 2024

@author: conductor
"""
from django.shortcuts import render
from .model import CalculatorForm

def index(request):
    return render(request, "index.html")

def calculator(request):
    form = CalculatorForm()
    result = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            expression = form.cleaned_data['expression']
            try:
                result = float(eval(expression))
            except Exception as e:
                result = 'Error: ' + str(e)
    return render(request, 'calculator.html', {'form': form, 'result': result})
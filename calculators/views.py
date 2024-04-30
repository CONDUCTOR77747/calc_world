# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:17:08 2024

@author: conductor
"""

from django.shortcuts import render
from .forms import CalculatorForm, QuadraticForm
from .models import Calculator

def index(request):
    calculators_count = Calculator.objects.count()
    calculators = Calculator.objects.all()
    
    response = {
                "calculators_count": calculators_count,
                "calculators": calculators,
                }
    
    return render(request, "index.html", context=response)

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
                result = 'Ошибка: проверьте правильность введённых данных'
    return render(request, 'calculators/calculator_regular.html', {'form': form, 'result': result})

def quadratic_solver(request):
    calc_page = 'calculators/quadratic/calculator_quadratic_equation.html'
    result_page = 'calculators/quadratic/result.html'
    form = QuadraticForm(request.POST or None)
    if form.is_valid():
        a = float(form.cleaned_data['a'])
        b = float(form.cleaned_data['b'])
        c = float(form.cleaned_data['c'])
        
        if a == 0:
            form.add_error('a', 'Коэффициент "a" не может быть 0')
            return render(request, calc_page, {'form': form})
        
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)
            result = f"Корни уравнения: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}"
        elif discriminant == 0:
            x = -b / (2 * a)
            result = f"Дискриминант равен нулю. Найден один корень уравнения: x = {round(x, 2)}"
        else:
            result = "Уравнение не имеет действительных корней"
        
        response = {
                    "a": a,
                    "b": b,
                    "c": c,
                    "result": result,
                    }
        
        return render(request, result_page, context=response)
    
    return render(request, calc_page, {'form': form})
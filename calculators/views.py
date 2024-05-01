# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:17:08 2024

@author: conductor
"""

from django.shortcuts import render, redirect
from .calculators_works import CalculatorForm, QuadraticForm
from .models import Calculator
from urllib.parse import quote, unquote

def index(request):
    calculators_count = Calculator.objects.count()
    calculators = Calculator.objects.all()
    
    response = {
                "calculators_count": calculators_count,
                "calculators": calculators,
                }
    
    return render(request, "index.html", context=response)

def encode_slashes(url):
    return url.replace('/', 'slash')

def decode_slashes(url):
    return url.replace('slash', '/')

def calculator(request):
    form = CalculatorForm()
    result = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            expression = form.cleaned_data['expression']
            result = float(eval(expression))
            expression_coded = encode_slashes(quote(f"{result} {expression}"))
            print("check", f'regular/result/{expression_coded}')
            return redirect(f'regular/result/{expression_coded}', expression_coded)
    
    return render(request, 'calculators/regular/calculator_regular.html', {"form": form})

def calculator_result(request, params):
    expression_decoded = decode_slashes(unquote(params)).split()
    response = {
                "result": expression_decoded[0],
                "expression": "".join(expression_decoded[1:]),
                }
    if request.method == 'POST':
        # save_result_to_db()
        print(expression_decoded)
    return render(request, 'calculators/regular/result.html', context=response)

def quadratic_solver(request):
    calc_page = 'calculators/quadratic/calculator_quadratic_equation.html'
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
                
        expression = quote(f"{a} {b} {c} {result}")
        return redirect(f'quadratic/result/{expression}', expression)
    
    return render(request, calc_page, {'form': form})

# def save_result_to_db(URL):
    

def quadratic_solver_result(request, params):
    expression_decoded = unquote(params).split()
    response = {
                "a": expression_decoded[0],
                "b": expression_decoded[1],
                "c": expression_decoded[2],
                "result": " ".join(expression_decoded[3:]),
                }
    
    if request.method == 'POST':
        # save_result_to_db()
        print("saved", expression_decoded)
    return render(request, 'calculators/quadratic/result.html', context=response)
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:01:11 2024

@author: conductor
"""
from django import forms
from django.core.validators import RegexValidator
from urllib.parse import unquote
from datetime import datetime
from .models import Solution, Calculator
import re

class CalculatorForm(forms.Form):
    expression = forms.CharField(label='Введите выражение', max_length=100)
    
    def clean_expression(self):
       expression = self.cleaned_data['expression']
       
       if not re.match(r'^[0-9+\-*\/().\s]*$', expression):
           raise forms.ValidationError('Разрешены только числа и операторы')

       try:
           eval(expression, {'__builtins__': {}}, {})
       except Exception:
           raise forms.ValidationError('Нельзя использовать несколько операторов подряд или не закрыты скобки')
       
       return expression

class QuadraticForm(forms.Form):
    a = forms.FloatField(label='Коэффициент a')
    b = forms.FloatField(label='Коэффициент b')
    c = forms.FloatField(label='Коэффициент c')
    
def save_solution(calculator_id, result):
    try:
        calculator = Calculator.objects.get(id=calculator_id)
    except Calculator.DoesNotExist:
        print(f"Калькулятор с id={calculator_id} не найден.")
        return
    
    solution = Solution.objects.create(calculator=calculator, time=datetime.now(), URL=calculator.URL)
    solution.save()

    return solution

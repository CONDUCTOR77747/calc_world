# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:01:11 2024

@author: conductor
"""
from django import forms
from django.core.validators import RegexValidator

class CalculatorForm(forms.Form):
    NumericValidator = RegexValidator(r'^[0-9+\-*\/() ]*$', 'Разрешены только числа и операторы')
    expression = forms.CharField(label='Введите выражение', 
                                 max_length=100, 
                                 validators=[NumericValidator])

class QuadraticForm(forms.Form):
    a = forms.FloatField(label='Коэффициент a')
    b = forms.FloatField(label='Коэффициент b')
    c = forms.FloatField(label='Коэффициент c')
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:01:11 2024

@author: conductor
"""

import re
from django import forms

class CalculatorForm(forms.Form):
    expression = forms.CharField(label='Введите выражение', max_length=100)

    def clean_expression(self):
        expression = self.cleaned_data['expression']

        if not re.match(r'^[0-9+\-*\/().\s]*$', expression):
            raise forms.ValidationError('Разрешены только числа и операторы')

        try:
            eval(expression, {'__builtins__': {}}, {})
        except Exception:
            raise forms.ValidationError(
                'Нельзя использовать несколько операторов подряд или не закрыты скобки')

        return expression


class QuadraticForm(forms.Form):
    a = forms.FloatField(label='Коэффициент a')
    b = forms.FloatField(label='Коэффициент b')
    c = forms.FloatField(label='Коэффициент c')

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:01:11 2024

@author: conductor
"""
from django import forms

class CalculatorForm(forms.Form):
    expression = forms.CharField(label='Expression', max_length=100)
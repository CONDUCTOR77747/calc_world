# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:17:08 2024

@author: conductor
"""
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
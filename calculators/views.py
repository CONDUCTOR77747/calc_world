"""
Author: Ammosov Yaroslav
Description: Views file contains render functions for html pages
"""

from urllib.parse import quote, unquote
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from simpleeval import simple_eval
from .models import Solution
from .forms import CalculatorForm, QuadraticForm
from .utils import encode_slashes, decode_slashes, save_solution, reset_table


def index(request):
    """
    Render and update main page

    Parameters
    ----------
    request : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    solutions_count = Solution.objects.count()
    solutions = Solution.objects.all().order_by('-id')
    response = {
        "solutions_count": solutions_count,
        "solutions": solutions,
    }
    if request.method == 'POST':
        reset_table(Solution)
        return HttpResponseRedirect("/")
    return render(request, "index.html", context=response)


def calculator(request):
    """
    Render and update regular calculator page

    Parameters
    ----------
    request : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    form = CalculatorForm()
    result = None
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            expression = form.cleaned_data['expression']
            result = float(simple_eval(expression))
            expression_coded = encode_slashes(quote(f"{result} {expression}"))
            return redirect(f'regular/result/{expression_coded}',
                            expression_coded)

    return render(request, 'calculators/regular/calculator_regular.html',
                  {"form": form})


def calculator_result(request, params):
    """
    Render and update regular calculator result page

    Parameters
    ----------
    request : TYPE
        DESCRIPTION.
    params : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    expression_decoded = decode_slashes(unquote(params)).split()
    response = {
        "result": expression_decoded[0],
        "expression": "".join(expression_decoded[1:]),
    }
    if request.method == 'POST':
        save_solution(Solution, request.build_absolute_uri())
        return HttpResponseRedirect("/")
    return render(request, 'calculators/regular/result.html', context=response)


def quadratic_solver(request):
    """
    Render and update quadratic calculator page

    Parameters
    ----------
    request : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    calc_page = 'calculators/quadratic/calculator_quadratic_equation.html'
    form = QuadraticForm(request.POST or None)
    if form.is_valid():
        coeff_a = float(form.cleaned_data['a'])
        coeff_b = float(form.cleaned_data['b'])
        coeff_c = float(form.cleaned_data['c'])

        if coeff_a == 0:
            form.add_error('a', 'Коэффициент "a" не может быть 0')
            return render(request, calc_page, {'form': form})

        discriminant = coeff_b ** 2 - 4 * coeff_a * coeff_c
        if discriminant > 0:
            x_1 = (-coeff_b + discriminant ** 0.5) / (2 * coeff_a)
            x_2 = (-coeff_b - discriminant ** 0.5) / (2 * coeff_a)
            result = f"Корни уравнения: x_1 = {round(x_1, 2)}, \
x_2 = {round(x_2, 2)}"
        elif discriminant == 0:
            single_x = -coeff_b / (2 * coeff_a)
            result = f"Дискриминант равен нулю. Найден один \
корень уравнения: single_x = {round(single_x, 2)}"
        else:
            result = "Уравнение не имеет действительных корней"

        expression = quote(f"{coeff_a} {coeff_b} {coeff_c} {result}")
        return redirect(f'quadratic/result/{expression}', expression)

    return render(request, calc_page, {'form': form})


def quadratic_solver_result(request, params):
    """
    Render and update quadratic calculator result page

    Parameters
    ----------
    request : TYPE
        DESCRIPTION.
    params : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    expression_decoded = unquote(params).split()
    response = {
        "a": expression_decoded[0],
        "b": expression_decoded[1],
        "c": expression_decoded[2],
        "result": " ".join(expression_decoded[3:]),
    }

    if request.method == 'POST':
        save_solution(Solution, request.build_absolute_uri())
        return HttpResponseRedirect("/")
    return render(request, 'calculators/quadratic/result.html',
                  context=response)

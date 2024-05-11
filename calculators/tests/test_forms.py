"""
Author: Ammosov Yaroslav
Description: This module contains test for forms
"""

from ..forms import CalculatorForm, QuadraticForm


def test_reg_calc_valid() -> None:
    """
    Test regular calculator with valid data

    Returns
    -------
    None.

    """
    valid_expression = '2 + 3 * (4 - 1)'
    form = CalculatorForm(data={'expression': valid_expression})
    assert form.is_valid()


def test_reg_calc_invalid() -> None:
    """
    Test regular calculator with invalid data

    Returns
    -------
    None.

    """
    invalid_expression = '2 + * 3'
    form = CalculatorForm(data={'expression': invalid_expression})
    assert not form.is_valid()
    assert 'Нельзя использовать несколько операторов \
подряд или не закрыты скобки' in form.errors['expression']
    invalid_expression2 = 'Hello World!'
    form2 = CalculatorForm(data={'expression': invalid_expression2})
    assert 'Разрешены только числа и операторы' in form2.errors['expression']


def test_quad_calc_valid() -> None:
    """
    Test qudaratic calculator with valid data

    Returns
    -------
    None.

    """
    valid_coefficients = {'a': 1, 'b': 2, 'c': 1}
    form = QuadraticForm(data=valid_coefficients)
    assert form.is_valid()


def test_quad_calc_invalid() -> None:
    """
    Test qudaratic calculator with invalid data

    Returns
    -------
    None.

    """
    invalid_coefficients = {'a': 'a', 'b': 'b', 'c': 'c'}
    form = QuadraticForm(data=invalid_coefficients)
    assert not form.is_valid()

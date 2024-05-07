"""
Forms for calculators
"""
import re
from simpleeval import simple_eval
from django import forms


class CalculatorForm(forms.Form):
    """
    Form for regular calculator
    """
    expression = forms.CharField(label='Введите выражение', max_length=100)

    def clean_expression(self) -> str:
        """
        Validation function of user input for regular calculator.

        Raises
        ------
        forms
            Forms for  calculators.

        Returns
        -------
        expression : str
            mathematical  expression.

        """
        expression = self.cleaned_data['expression']

        if not re.match(r'^[0-9+\-*\/().\s]*$', expression):
            raise forms.ValidationError('Разрешены только числа и операторы')

        try:
            simple_eval(expression)
        except Exception as e:
            raise forms.ValidationError(
                'Нельзя использовать несколько \
операторов подряд или не закрыты скобки') from e

        return expression


class QuadraticForm(forms.Form):
    """
    Form for quadratic equation calculator
    """
    a = forms.FloatField(label='Коэффициент a')
    b = forms.FloatField(label='Коэффициент b')
    c = forms.FloatField(label='Коэффициент c')

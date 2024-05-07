"""
Forms for calculators
"""
import re
from django import forms


class CalculatorForm(forms.Form):
    """
    Form for regular calculator
    """
    expression = forms.CharField(label='Введите выражение', max_length=100)

    def clean_expression(self) -> str:
        """


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
            eval(expression, {'__builtins__': {}}, {})
        except Exception:
            raise forms.ValidationError(
                'Нельзя использовать несколько \
операторов подряд или не закрыты скобки')

        return expression


class QuadraticForm(forms.Form):
    """
    Form for quadratic equation calculator
    """
    a = forms.FloatField(label='Коэффициент a')
    b = forms.FloatField(label='Коэффициент b')
    c = forms.FloatField(label='Коэффициент c')

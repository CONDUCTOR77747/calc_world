"""
Author: Ammosov Yaroslav
Description: This module contains test for views
"""

from urllib.parse import quote
import typing
import pytest
from django.test import Client
from ..models import Solution
from ..utils import save_solution


@pytest.mark.django_db
def test_index_view(client: Client) -> None:
    """
    Test index page, get request.

    Parameters
    ----------
    client : Client
        An instance of the Client class.

    Returns
    -------
    None.

    """
    response = client.get("")
    assert response.status_code == 200


@pytest.mark.django_db
def test_index_post(client: Client) -> None:
    """
    Test index page, post request.

    Parameters
    ----------
    client : Client
        An instance of the Client class.

    Returns
    -------
    None.

    """
    url = "https://test.com"
    save_solution(Solution, url)

    response = client.post("")
    assert response.status_code == 302  # Redirects after POST (refresh page)
    assert Solution.objects.count() == 0  # reset table


def test_calculator_view(client: Client) -> None:
    """
    Test regular calculator page, get request.

    Parameters
    ----------
    client : Client
        An instance of the Client class.

    Returns
    -------
    None.

    """
    response = client.get("/regular")
    assert response.status_code == 200
    assert 'form' in response.context


def test_calculator_post_invalid(client: Client) -> None:
    """
    Test regular calculator page, post request, invalid data.

    Parameters
    ----------
    client : Client
        An instance of the Client class.

    Returns
    -------
    None.

    """
    response = client.post("/regular", {'expression': '2+invalid'})
    assert response.status_code == 200  # Should stay on the same page
    assert 'form' in response.context
    assert ('Разрешены только числа и операторы' in
            response.context['form'].errors['expression'])


@pytest.mark.django_db
def test_calculator_post_valid(client: Client) -> None:
    """
    Test regular calculator page, post request, valid data.
    Full cycle test.

    Parameters
    ----------
    client : Client
        An instance of the Client class.

    Returns
    -------
    None.

    """
    # Test post regular calculator page
    response = client.post("/regular", {'expression': '2+2/2'})
    assert response.status_code == 302  # Redirects after POST

    # Test result page render
    url_raw = typing.cast(str | None, getattr(response, 'url', None))
    url = quote(f"/{url_raw}")
    response_get = client.get(url)
    assert response_get.status_code == 200
    assert 'result' in response_get.context
    assert '3.0' in response_get.context['result']

    # Test result page post request
    response = client.post(url)
    assert response.status_code == 302
    saved_solution = Solution.objects.get(id=1)
    assert saved_solution.time is not None
    assert saved_solution.URL == 'http://testserver'+url


def test_quadratic_solver_view(client: Client) -> None:
    """
    Test regular calculator page, post request, valid data.

    Parameters
    ----------
    client : Client
        An instance of the Client class.

    Returns
    -------
    None.

    """
    response = client.get("/quadratic/")
    assert response.status_code == 200
    assert 'form' in response.context


def test_quadratic_solver_post_invalid(client: Client) -> None:
    """
    Test quadratic calculator page, post request, invalid data.
    Check for error message for coefficient 'a'.

    Parameters
    ----------
    client : Client
        An instance of the Client class.

    Returns
    -------
    None.

    """
    response = client.post("/quadratic/", {'a': 0, 'b': 0, 'c': 0})
    assert response.status_code == 200  # Should stay on the same page
    assert 'form' in response.context
    assert ('Коэффициент "a" не может быть 0'
            in response.context['form'].errors['a'])


def test_quadratic_solver_post_valid(client: Client) -> None:
    """
    Test quadratic calculator page, post request, valid data.
    Check if submit button works and redirecs to result page.

    Parameters
    ----------
    client : Client
        An instance of the Client class.

    Returns
    -------
    None.

    """
    response = client.post("/quadratic/", {'a': 1, 'b': -3, 'c': 2})
    assert response.status_code == 302  # Redirects after POST


@pytest.mark.django_db
def test_quadratic_solver_post_discriminant_zero(client: Client) -> None:
    """
    Test quadratic calculator page, post request, valid data.
    Testing discriminant equals zero case.
    Full cycle test.

    Parameters
    ----------
    client : Client
        An instance of the Client class.
    Returns
    -------
    None.

    """
    response = client.post("/quadratic/", {'a': 1, 'b': -2, 'c': 1})
    assert response.status_code == 302  # Redirects after POST

    # Test result page render
    url = quote(typing.cast(str, getattr(response, 'url', None)))
    response_get = client.get(url)
    assert response_get.status_code == 200
    assert 'result' in response_get.context
    assert ('Дискриминант равен нулю. Найден один корень уравнения: x = 1.0'
            in response_get.context['result'])

    # Test result page post request
    response = client.post(url)
    assert response.status_code == 302
    saved_solution = Solution.objects.get(id=1)
    assert saved_solution.time is not None
    assert saved_solution.URL == 'http://testserver'+url


@pytest.mark.django_db
def test_quadratic_solver_post_discriminant_positive(client: Client) -> None:
    """
    Test quadratic calculator page, post request, valid data.
    Testing positive discriminant case.
    Full cycle test.

    Parameters
    ----------
    client : Client
        An instance of the Client class.

    Returns
    -------
    None.

    """
    response = client.post("/quadratic/", {'a': 1, 'b': -5, 'c': 6})
    assert response.status_code == 302  # Redirects after POST

    # Test result page render
    url = quote(typing.cast(str, getattr(response, 'url', None)))
    response_get = client.get(url)
    assert response_get.status_code == 200
    assert 'result' in response_get.context
    assert ('Корни уравнения: x_1 = 3.0, x_2 = 2.0'
            in response_get.context['result'])

    # Test result page post request
    response = client.post(url)
    assert response.status_code == 302
    saved_solution = Solution.objects.get(id=1)
    assert saved_solution.time is not None
    assert saved_solution.URL == 'http://testserver'+url


@pytest.mark.django_db
def test_quadratic_solver_post_discriminant_negative(client: Client) -> None:
    """
    Test quadratic calculator page, post request, valid data.
    Testing negative discriminant case.
    Full cycle test.

    Parameters
    ----------
    client : Client
        An instance of the Client class.

    Returns
    -------
    None.

    """
    response = client.post("/quadratic/", {'a': 1, 'b': 2, 'c': 3})
    assert response.status_code == 302  # Redirects to result page

    # Test result page render
    url = quote(typing.cast(str, getattr(response, 'url', None)))
    response_get = client.get(url)
    assert response_get.status_code == 200
    assert 'result' in response_get.context
    assert ('Уравнение не имеет действительных корней'
            in response_get.context['result'])

    # Test result page post request
    response = client.post(url)
    assert response.status_code == 302
    saved_solution = Solution.objects.get(id=1)
    assert saved_solution.time is not None
    assert saved_solution.URL == 'http://testserver'+url

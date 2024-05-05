"""
Model contains functions for encoding url, saving and resetting database
"""

from typing import Type
from django.utils import timezone
from django.db import connection, transaction
from .models import Solution


def encode_slashes(str_: str) -> str:
    """
    Replaces slashes in string with word "slash"

    Parameters
    ----------
    url : str
        string object.

    Returns
    -------
    str
        string object.

    """
    return str_.replace('/', 'slash')


def decode_slashes(url: str) -> str:
    """
    Replaces words "slash" in string with slashes

    Parameters
    ----------
    url : str
        string object.

    Returns
    -------
    str
        string object.

    """
    return url.replace('slash', '/')


def save_solution(model: Type[Solution], url: str) -> None:
    """
    Saves data to database with solutions history

    Parameters
    ----------
    model : Type[Solution]
        model of database for storring solutions history.
    url : str
        url addres for calculator with params.

    Returns
    -------
    None.

    """
    current_datetime = timezone.now()
    solution = model.objects.create(time=current_datetime, URL=url)
    solution.save()


def reset_table(model: Type[Solution]) -> None:
    """
    Delets all objects from solutions history and sets autoincrement to 1.

    Parameters
    ----------
    model : Type[Solution]
        model of database for storring solutions history.

    Returns
    -------
    None.

    """
    with transaction.atomic():
        model.objects.all().delete()
        with connection.cursor() as cursor:
            table_name = model._meta.db_table  # pylint: disable=W0212
            cursor.execute(f"DELETE FROM sqlite_sequence\
                             WHERE name='{table_name}';")

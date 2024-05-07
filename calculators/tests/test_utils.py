"""
This module contains test for utils
"""

import pytest
from django.utils import timezone
from ..models import Solution
from ..utils import encode_slashes, decode_slashes, save_solution, reset_table


def test_encode_slashes() -> None:
    """
    Test encode_slashes function

    Returns
    -------
    None.

    """
    url = "https://test.com/path/to/res"
    encoded_url = encode_slashes(url)
    assert encoded_url == "https:slashslashtest.comslashpathslashtoslashres"


def test_decode_slashes() -> None:
    """
    Test decode_slashes function

    Returns
    -------
    None.

    """
    encoded_url = "https:slashslashtest.comslashpathslashtoslashresource"
    decoded_url = decode_slashes(encoded_url)
    assert decoded_url == "https://test.com/path/to/resource"


@pytest.mark.django_db
def test_save_solution() -> None:
    """
    Test save_solution function

    Returns
    -------
    None.

    """
    url = "https://test.com"
    save_solution(Solution, url)
    saved_solution = Solution.objects.get(id=1)
    assert saved_solution.time is not None
    assert saved_solution.URL == "https://test.com"


@pytest.mark.django_db
def test_reset_table() -> None:
    """
    Test reset_table function

    Returns
    -------
    None.

    """
    url = "https://test.com"
    save_solution(Solution, url)
    reset_table(Solution)
    assert Solution.objects.count() == 0

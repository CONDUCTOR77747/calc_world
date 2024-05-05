"""
This module contains test for models
"""

import pytest
from django.utils import timezone
from ..models import Solution


@pytest.mark.django_db
def test_solution_creation() -> None:
    """
    Test for model. Creates database and checks if it works.

    Returns
    -------
    None.

    """
    solution = Solution.objects.create(
        time=timezone.now(),
        URL="https://test.com"
    )

    saved_solution = Solution.objects.get(id=solution.id)
    assert solution.time == saved_solution.time
    assert solution.URL == saved_solution.URL
    assert str(solution) == f"{solution.id}-{solution.time}-{solution.URL}"

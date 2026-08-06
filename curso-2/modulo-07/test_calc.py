"""Test que se ejecutará en el CI de GitHub Actions."""

from calc import sumar


def test_sumar():
    assert sumar(2, 3) == 5

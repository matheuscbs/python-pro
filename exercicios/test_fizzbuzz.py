import pytest

from exercicios.fizzbuzz import fizzbuzz


@pytest.mark.parametrize("input_value, expected_output", [
    (15, "FizzBuzz"),  # Divisível por 3 e 5
    (30, "FizzBuzz"),  # Divisível por 3 e 5
    (3, "Fizz"),       # Divisível por 3
    (9, "Fizz"),       # Divisível por 3
    (5, "Buzz"),       # Divisível por 5
    (20, "Buzz"),      # Divisível por 5
    (1, "1"),          # Não divisível por 3 ou 5
    (7, "7"),          # Não divisível por 3 ou 5
    (13, "13"),        # Não divisível por 3 ou 5
])
def test_fizzbuzz(input_value, expected_output):
    assert fizzbuzz(input_value) == expected_output

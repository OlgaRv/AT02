import pytest

# первый пример
def test_add():
    assert  1 + 1 == 2, "Should be 2"

def test_subtract():
    assert  3 - 2 == 1, "Should be 1"

# второй пример

def check(number):
    return number % 2 == 0

# третий пример - палиндром
def is_palindrome(string):
    return string == string[::-1]

# четвертый пример
def sort_list(numbers):
    return sorted(numbers)
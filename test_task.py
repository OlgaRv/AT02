# сравнение unittest и pytest

# первый пример
import unittest

class Testmath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
        self.assertEqual(1 + 1, 2, "Should be 2")
    def test_subtract(self):
        self.assertEqual(3-2, 1, "Should be 1")

# второй пример
import pytest
from main_task import check

def test_check():
    assert check(6) == True
    assert check(3) == False

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (5, False),
    (0, True),
    (56, True),
    (-3, False)
])

def test_check_with_params(number, expected):
    assert check(number) == expected

#  третий пример

from main_task import is_palindrome

def test_is_palindrome_True():
    assert is_palindrome("madam") == True

def test_is_palindrome_False():
    assert is_palindrome("hello") == False

@pytest.mark.parametrize("text_input, expected", [
    ("level", True),
    ("python", False),
    ("racecar", True),
    ("12321", True),
    ("12345", False),
    ("", True)
])

def test_is_palindrome_with_param(text_input, expected):
    assert is_palindrome(text_input) == expected

# четвертый пример

from main_task import sort_list

def test_sort1():
    assert sort_list([5, 6, 3, 2, 1]) == [1, 2, 3, 5, 6]

def test_sort2():
    assert sort_list([1, 0, -2, -1, 3]) == [-2, -1, 0, 1, 3]
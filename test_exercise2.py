#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"


def test_find_added():
    """
    Test find function.
    """
    # substring is found:
    # index provided is out of range
    assert find("This is an ex-parrot", "parrot", 0, 25) == 14
    # substring appears in several locations
    assert find("This is an ex-parrot parrot", "parrot", 0, 20) == 14
    # end, start contain negative numbers but slicing notation does not give empty result
    assert find("This is an ex-parrot.", "parrot", 0, -1) == 14
    assert find("This is an ex-parrot.", "parrot", -20, -1) == 14

    # substring is not found:
    # slicing notation gives empty result
    assert find("This is an ex-parrot", "parrot", 15, -6) == -1
    assert find("This is an ex-parrot", "parrot", 20, 0) == -1
    # end index is not included
    assert find("This is an ex-parrot", "parrot", 0, 14) == -1
    # ( end - start ) is less than the length of a substring
    assert find("This is an ex-parrot", "parrot", 14, 19) == -1
    # case sensitive
    assert find("This is an ex-Parrot", "parrot", 0, 20) == -1
    # word is separated by other notations:
    assert find("This is an par r o t", "parrot", 0, 20) == -1


def test_multi_find_added():
    """
    Test multi_find function.
    """
    # substring is found:
    # index provided is out of range
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni!", 1, 25) == "4,8,12"
    # substring appears one time; case sensitive
    assert multi_find("NI! NI! NI! Ni!", "Ni!", 0, 15) == "12"
    # end, start contain negative numbers, slicing notation does not give empty result
    assert multi_find("Ni! Ni! Ni! Ni!!", "Ni", 0, -1) == "0,4,8,12"
    assert multi_find("Ni! Ni! Ni! Ni!!", "Ni", -16, -1) == "0,4,8,12"

    # substring is not found:
    # slicing notation gives empty result, (end index is not included)
    assert multi_find("Ni! Ni! Ni! Ni!!", "Ni", 9, -9) == ""
    assert multi_find("Ni! Ni! Ni! Ni!!", "Ni", 0, 1) == ""
    # (end - start) is less than the length of substring
    assert multi_find("Ni! Ni! Ni! Ni!!", "Ni!", 0, 2) == ""
    # word is separated by other notations:
    assert multi_find("Ni! Ni! Ni! Ni!!", "N i", 0, 15) == ""









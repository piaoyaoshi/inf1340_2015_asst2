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

    # end index provided is out of range
    assert find("This is an ex-parrot", "parrot", 0, 25) == 14
    assert find("Happy anniversary", "ann", 0, 25) == 6

    # substring appears in several locations
    assert find("This is an ex-parrot parrot", "parrot", 0, 20) == 14
    assert find("Happy anniversary Happy anniversary", "ann", 0, 35) == 6

    # end, start contain negative numbers but slicing notation does not give empty result
    assert find("This is an ex-parrot.", "parrot", 0, -1) == 14
    assert find("This is an ex-parrot.", "parrot", -20, -1) == 14
    assert find("Happy anniversary", "ann", 0, -2) == 6
    assert find("Happy anniversary", "ann", -15, -1) == 6

    # substring is not found:

    # start index provided is out of range.
    assert find("This is an ex-parrot", "parrot", 20, 25) == -1
    assert find("Happy anniversary", "ann", 17, 25) == -1

    # slicing notation gives empty result
    assert find("This is an ex-parrot", "parrot", 15, -6) == -1
    assert find("This is an ex-parrot", "parrot", 20, 0) == -1
    assert find("Happy anniversary", "ann", 6, -11) == -1
    assert find("Happy anniversary", "ann", -5, -6) == -1

    # input_string[start:end] not includes substring
    assert find("This is an ex-parrot", "parrot", 0, 14) == -1   # end is not included.
    assert find("Happy anniversary", "ann", 0, 8) == -1
    assert find("This is an ex-parrot", "parrot", 14, 19) == -1  # ( end - start ) is less than the len(substring)
    assert find("Happy anniversary", "ann", 6, 8) == -1

    # case sensitive
    assert find("This is an ex-Parrot", "parrot", 0, 20) == -1
    assert find("Happy anniversary", "Ann", 0, 16) == -1

    # word is separated by other notations:
    assert find("This is an par r o t", "parrot", 0, 20) == -1
    assert find("Happy anniversary", "a nn", 0, 16) == -1


def test_multi_find_added():
    """
    Test multi_find function.
    """
    # substring is found:

    # end index provided is out of range
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni!", 1, 25) == "4,8,12"
    assert multi_find("Happy anniversary Happy anniversary", "ann", 0, 38) == "6,24"

    # substring appears one time; case sensitive
    assert multi_find("NI! NI! NI! Ni!", "Ni!", 0, 15) == "12"
    assert multi_find("Happy anniversary Happy Anniversary", "Ann", 0, 34) == "24"

    # end, start contain negative numbers, slicing notation does not give empty result
    assert multi_find("Ni! Ni! Ni! Ni!!", "Ni", 0, -1) == "0,4,8,12"
    assert multi_find("Ni! Ni! Ni! Ni!!", "Ni", -16, -1) == "0,4,8,12"
    assert multi_find("Happy anniversary Happy anniversary", "ann", 0, -1) == "6,24"
    assert multi_find("Happy anniversary Happy anniversary", "ann", -30, -5) == "6,24"

    # substring is not found:

    # slicing notation gives empty result, (end index is not included)
    assert multi_find("Ni! Ni! Ni! Ni!!", "Ni", 9, -9) == ""
    assert multi_find("Ni! Ni! Ni! Ni!!", "Ni", 0, 1) == ""
    assert multi_find("Happy anniversary Happy anniversary", "ann", -15, 15) == ""

    # (end - start) is less than the length of substring
    assert multi_find("Ni! Ni! Ni! Ni!!", "Ni!", 0, 2) == ""
    assert multi_find("Happy anniversary Happy anniversary", "ann", 6, 8) == ""

    # word is separated by other notations:
    assert multi_find("N!i N!i N!i N!i!", "Ni", 0, 15) == ""
    assert multi_find("Happy anniversary Happy anniversary", "ann!", 0, 38) == ""









#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    Return the lowest index in input_string where substring is found,
    such that substring is wholly contained in input_string[start:end].
    Arguments start and end are required and interpreted as in slice notation.

    Return -1 if substring is not found.

    :param :input_string: a string
            substring:    a string
            start:        an int
            end:          an int
    :return:lowest i :    an int
    :raises:none

    """

    target_str = input_string[start:end]                      # use standard slice notation.

    for i in range(0, len(target_str) - len(substring) + 1):  # no need to check if len(remaining str) < len(substring)
        if target_str[i: i + len(substring)] == substring:    # compare strings in whole.
            return i + len(input_string[:start])

    return -1


def multi_find(input_string, substring, start, end):
    """(str, str, num, num) --> str
    Return all indices in the input_string[start: end] where the substring is found.
    Indices are displayed in a string, and separated by commas.
    Arguments start and end are required and interpreted as in slice notation.

    Return an empty string if the substring is not found.

    :param :input_string: a string
            substring:    a string
            start:        an int
            end:          an int
    :return:result :      a string
    :raises:none
    """

    result = ''
    i = find(input_string, substring, start, end)  # call function find to avoid code duplication.
    while i != -1:
        result += str(i) + ','
        # search again from 1 position left of the previous index (to avoid infinite loop).
        i = find(input_string, substring, i + 1, end)
    if len(result):                               # condition is true if result is not an empty string, otherwise false.
        return result[:-1]                        # do not include the last comma
    return result

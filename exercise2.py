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
    such that substring is contained within input_string[start:end]. required
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure

    :param : input_string: a string
             substring:    a string
             start:        an int
             end:          an int
    :return: lowest i :    an int
    :raises:

    """

    s = input_string[start:end]
    for i in range(0, len(s) - len(substring) + 1):
        if s[i: i + len(substring)] == substring:
            return i + len(input_string[:start])
    return -1


def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""

    return result


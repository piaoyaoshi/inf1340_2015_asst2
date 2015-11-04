#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise3 import union, intersection, difference, MismatchedAttributesException


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

HEADER = [["Number", "Surname", "Age"]]

EMPTY = [[]]

STAFFS = [["Number", "First Name", "Surname", "Date of Birth"],
          [9297, "Andy", "O'Malley", "56"],
          [7432, "Barbara", "O'Malley", "39"],
          [9824, "Carl", "Darkes", "38"]]
#####################
# HELPER FUNCTIONS ##
#####################


def is_equal(t1, t2):
    return set(map(tuple, t1)) == set(map(tuple, t2))


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))


def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))


def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))

# ==================================== Test cases added, schema are the same ==========================================


def test_union_added_1():
    """
    Test union operation.
    """
    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, HEADER))


def test_union_2():
    """
    Test union operation. Table 1 is the MANAGERS table; Table 2 is the GRADUATES table
    """

    result = [["Number", "Surname", "Age"],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38],
              [7274, "Robinson", 37]]

    assert is_equal(result, union(MANAGERS, GRADUATES))


def test_intersection_added_1():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"]]

    assert is_equal(result, intersection(GRADUATES, HEADER))


def test_difference_added_1():      # table 2 only has a header
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, difference(GRADUATES, HEADER))


def test_difference_added_2():     # table 1 only has a header
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"]]

    assert is_equal(result, difference(HEADER, GRADUATES))


# ===================================== Schema are different  =========================================================

def test_union_different_schema_1():
    """
    Test union operation.Scheme are not the same
    """
    try:
        union(MANAGERS, STAFFS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False


def test_intersection_different_schema_1():
    """
    Test intersection operation. Scheme are not the same.
    """
    try:
        intersection(MANAGERS, STAFFS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False


def test_difference_different_schema_1():
    """
    Test difference operation. Scheme are not the same.
    """
    try:
        difference(MANAGERS, STAFFS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False


def test_union_different_schema_2():
    """
    Test union operation.Scheme are not the same. Table2 only has a header.
    """
    try:
        union(MANAGERS, EMPTY)
    except MismatchedAttributesException:
        assert True
    else:
        assert False




def test_intersection_different_schema_2():
    """
    Test intersection operation. Scheme are not the same.Table2 only has a header.
    """
    try:
        intersection(MANAGERS, EMPTY)
    except MismatchedAttributesException:
        assert True
    else:
        assert False


def test_difference_different_schema_2():
    """
    Test difference operation. Scheme are not the same.Table2 only has a header.
    """
    try:
        difference(MANAGERS, EMPTY)
    except MismatchedAttributesException:
        assert True
    else:
        assert False
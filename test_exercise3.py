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

HEADER_ONLY = [["Number", "Surname", "Age"]]

NO_HEADER = [[]]

EMPTY_LIST = []

STAFFS = [["Number", "First Name", "Surname", "Date of Birth"],
          [9297, "Andy", "O'Malley", "56"],
          [7432, "Barbara", "O'Malley", "39"],
          [9824, "Carl", "Darkes", "38"]]

EMPLOYEES = [["Number", "Surname", "Age"],
             [1000, "Ann", 20],
             [1001, "Mary", 22],
             [1002, "Ming", 60]]

#####################
# HELPER FUNCTIONS ##
#####################


def is_equal(t1, t2):
    return sorted(t1) == sorted(t2)


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


def test_union_graduates_employees():
    """
    Test union operation. Table1 is the GRADUATES table; Table2 is the EMPLOYEES table.
    """
    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38],
              [1000, "Ann", 20],
              [1001, "Mary", 22],
              [1002, "Ming", 60]]

    assert is_equal(result, union(GRADUATES, EMPLOYEES))


def test_intersection_graduates_employees():
    """
    Test intersection operation.Table1 is the GRADUATES table; Table2 is the EMPLOYEES table.
    """

    assert intersection(GRADUATES, EMPLOYEES) is None


def test_difference_graduates_employees():
    """
    Test difference operation.Table1 is the GRADUATES table; Table2 is the EMPLOYEES table.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, difference(GRADUATES, EMPLOYEES))


def test_difference_employees_graduates():
    """
    Test difference operation.Table1 is the EMPLOYEES table; Table2 is the GRADUATES table.
    """

    result = [["Number", "Surname", "Age"],
              [1000, "Ann", 20],
              [1001, "Mary", 22],
              [1002, "Ming", 60]]

    assert is_equal(result, difference(EMPLOYEES, GRADUATES))


def test_union_graduates_header():
    """
    Test union operation. Table1 is the GRADUATES table; Table2 only has header, does not contain any record.
    """
    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, HEADER_ONLY))


def test_intersection_graduates_header():
    """
    Test intersection operation.Table1 is the GRADUATES table; Table2 only has header, does not contain any record.
    """
    assert intersection(GRADUATES, HEADER_ONLY) is None


def test_difference_graduates_header():
    """
    Test difference operation.Table1 is the GRADUATES table; Table2 only has header, does not contain any record.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, difference(GRADUATES, HEADER_ONLY))


def test_difference_header_graduates():
    """
    Test difference operation.Table1 only does not contain any record; Table2 is the GRADUATES table.
    """
    assert difference(HEADER_ONLY, GRADUATES) is None


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
        union(MANAGERS, NO_HEADER)
    except MismatchedAttributesException:
        assert True
    else:
        assert False


def test_intersection_different_schema_2():
    """
    Test intersection operation. Scheme are not the same.Table2 is empty.
    """
    try:
        intersection(MANAGERS, NO_HEADER)
    except MismatchedAttributesException:
        assert True
    else:
        assert False


def test_difference_different_schema_2():
    """
    Test difference operation. Scheme are not the same.Table2 is empty.
    """
    try:
        difference(MANAGERS, NO_HEADER)
    except MismatchedAttributesException:
        assert True
    else:
        assert False


# =================================== table1 or table2 is an empty list ===============================================


def test_union_graduates_empty():
    """
    Test union operation. Table1 is the GRADUATES table; Table2 is an empty list.
    """

    assert union(GRADUATES, EMPTY_LIST) is None


def test_intersection_graduates_empty():
    """
    Test intersection operation.Table1 is the GRADUATES table; Table2 is an empty list.
    """

    assert intersection(GRADUATES, EMPTY_LIST) is None


def test_difference_graduates_empty():
    """
    Test difference operation.Table1 is the GRADUATES table; Table2 is an empty list.
    """

    assert difference(GRADUATES, EMPTY_LIST) is None
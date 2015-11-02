#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

    result = table1[:]
    # same number of columns, the columns have the same names in the same order
    if table1[0] != table2[0]:
        raise MismatchedAttributesException
    else:
        for record in table2[1:]:  # order matters in a list; this line will not execute if table2 only has a header.
            if record not in result:
                result.append(record)
    return result


def intersection(table1, table2):
    """
    Return a new_table contains rows that appear both in table1 and table2.

    """

    result = []

    if table1[0] != table2[0]:
        raise MismatchedAttributesException
    else:
        for record in table1:
            # headers included
            if record in table2:
                result.append(record)
    return result


def difference(table1, table2):
    """
    Return a new_table contains rows that appear in table1 but not in table2.

    """

    result = [table1[0]]
    if table1[0] != table2[0]:
        raise MismatchedAttributesException
    else:
        for record in table1:
            # headers included
            if record not in table2:
                result.append(record)
    return result



#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass


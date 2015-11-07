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
    Return a result list that shows result of performing the union set operation on tables, table1 and table2.

    Return None if two tables do not have common record.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

    result = []

    if (len(table1) > 0 and len(table2) > 0) and check_headers(table1[0], table2[0]):
        # the following code will not execute if either table1 or table2 is empty or tables have different schema.
        result = table1[:]
        for record in table2[1:]:            # table2[1:] gives empty list, if table2 has no record/row
            if record not in result:
                result.append(record)
    if len(result) > 1:
        return result
    return None


def intersection(table1, table2):
    """
    Return a resulting list that contains rows that appear both in table1 and table2.

    Return None if two tables do not have common record.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

    result = []

    if (len(table1) > 0 and len(table2) > 0) and check_headers(table1[0], table2[0]):
        for record in table1:
            if record in table2:
                result.append(record)   # headers included after the first iteration
    if len(result) > 1:                 # if there is any records/row (header does not include)
        return result
    return None


def difference(table1, table2):
    """
    Return a resulting list that contains rows that appear in table1 but not in table2.

    Return None if two tables do not have common record.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """

    result = []

    if (len(table1) > 0 and len(table2) > 0) and check_headers(table1[0], table2[0]):
        result = [table1[0]]            # headers included in the result if table1 and table2 has the same schema.
        for record in table1:
            if record not in table2:
                result.append(record)
    if len(result) > 1:
        return result
    return None


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


def check_headers(header1, header2):
    """
    Return True if header1 and header2 have same number of columns, same names and same order.
    Raise MismatchedAttributesException otherwise.

    :param header1: headers (a List of strings)
    :param header2: headers (a List of strings)
    :return: boolean
    :raises: MismatchedAttributesException
    """

    if header1 != header2:
        raise MismatchedAttributesException
    return True


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass
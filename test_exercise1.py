#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise1 import pig_latinify


def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"


def test_our_basic():
    """
    Basic test cases added.
    """

    assert pig_latinify("if") == "ifyay"            # word starts with a vowel
    assert pig_latinify("world") == "orldway"       # vowel in middle
    assert pig_latinify("who") == "owhay"           # vowel at the end
    assert pig_latinify("where") == "erewhay"       # has more than one vowel
    assert pig_latinify("why") == "whyay"           # word with no vowel
    assert pig_latinify("") == ""                   # test empty string
    assert pig_latinify("yellow") == "ellowyay"     # test word begins with y

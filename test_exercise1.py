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
    # word starts with a vowel
    assert pig_latinify("if") == "ifyay"
    assert pig_latinify("all") == "allyay"

    # vowel in middle
    assert pig_latinify("world") == "orldway"
    assert pig_latinify("not") == "otnay"

    # vowel at the end
    assert pig_latinify("who") == "owhay"
    assert pig_latinify("the") == "ethay"

    # has more than one vowel
    assert pig_latinify("where") == "erewhay"
    assert pig_latinify("because") == "ecausebay"

    # word with no vowel
    assert pig_latinify("why") == "whyay"
    assert pig_latinify("cry") == "cryay"

    # word with capitalization
    assert pig_latinify("World") == "orldWay"
    assert pig_latinify("Not") == "otNay"

    # word with hyphen/dot
    assert pig_latinify("sugar-free") == "ugar-freesay"
    assert pig_latinify("good-hearted") == "ood-heartedgay"
    assert pig_latinify("i.e.") == "i.e.yay"
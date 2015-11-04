#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latin_translator(english):
    english = english.lower()
    result = ""
    vowel = "a,e,i,o,u"
    if english[0] is vowel:
        return result + "yay"
    while english[0] is not vowel:
        english[0] += (english[1:] + english[0])
        if english[0] == vowel:
            print result + "ay"
        else:
            return ""
print pig_latin_translator("test")


def pig_latin_translator():
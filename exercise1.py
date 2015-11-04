#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

latin_end = "ay"

english = raw_input("Enter an english word")

firstL = english[0]

latin_word = english + firstL + latin_end

latin_word = latin_word[1:]

print (latin_word)
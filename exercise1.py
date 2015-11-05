#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    Return a Pig Latin word based on the word given.
    If a word begins with a vowel, append 'yay' to the end of the word;
    If the word begins with a consonant, remove all the consonants from the beginning up to the first vowel and
    append them to the end of the word and append 'ay' to the end of the word.

    Parameter passed in has to be an English word.

    :param : word: a string
    :return: a new word : a string
    :raises:

    """

    result = ''
    vowel_index = -1

    for i in range(len(word)):
        if word[i] in 'aeiouAEIOU':
            vowel_index = i
            break                  # stop the loop when the first vowel is found.

    # now we have vowel_i
    if len(word) > 0:
        if vowel_index == 0:       # word begins with a vowel
            result = word + 'yay'
        elif vowel_index == -1:    # word contains no vowel, return the original word + 'ay"
            result = word + 'ay'
        else:                      # word has a mix of vowels and consonants
            result = word[vowel_index:] + word[0:vowel_index] + 'ay'

    return result


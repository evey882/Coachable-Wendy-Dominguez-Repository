"""125. Valid Palindrome"""

from typing import List

class Solution:
    """Solution Class"""

    def valid_palindrome(self, s: str):
        """
            This function determines if a passed string, which does not contain exclusive lower case
            alphabetic characters, is a valid palindrome. Meaning it reads the same forwards and backwards.
            Using this definition the string is broken into individual characters, lowercase and only alphabetic
            characters are stored. Since we only have to return a boolean we can return the comparison of the
            list of string forwards and backwards.
        """
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]
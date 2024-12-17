"""13. Roman to Integer"""

from collections import defaultdict

class Solution:
    "Solution Class"

    def romanToInt(self, s: str) -> int:
        """
        This function roman to integers takes in a string which represents a valid roman number
        and converts it to a base 10 integer. This is done with the use of a map containing the
        possible combinations and traversing the passed in string in one go.
        """
        roman_int = {
            "I" : 1,
            "IV": 4,
            "V" : 5,
            "IX": 9,
            "X" : 10,
            "XL" : 40,
            "L" : 50,
            "XC" : 90,
            "C" : 100,
            "CD" : 400,
            "D" : 500,
            "CM" : 900,
            "M" : 1000,
        }

        total = 0
        idx = 0

        while idx < len(s):
            if s[idx : idx + 2] in roman_int:
                total += roman_int[s[idx : idx + 2]]
                idx += 2
            else:
                total += roman_int[s[idx]]
                idx += 1

        return total
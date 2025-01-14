"""20. Valid Parentheses"""

from typing import List

class Solution:
    """Solution class"""

    def isValid(self, s: str) -> bool:
        """
            This function determines if the parentheses passed in are valid, meaning
            they are opened and closed in the appropriate order, this includes nested parentheses.
            It keeps a dictionary of the possible matches, and an array of the encountered opened
            brackets. If a closing bracket is encountered, then the corresponding open bracket
            should be at the end of the array, if this is not the case false is returned. If
            there are unclosed brackets in the array then false is returned also. Otherwise, it
            is a valid parentheses string.
        """

        brackets = {")":"(", "}":"{", "]":"["}
        opened_brackets_seen = []

        for bracket in s:
            if bracket in brackets:
                if opened_brackets_seen and opened_brackets_seen[-1] == brackets[bracket]:
                    opened_brackets_seen.pop()
                else:
                    return False
            else:
                opened_brackets_seen.append(bracket)

        return not opened_brackets_seen

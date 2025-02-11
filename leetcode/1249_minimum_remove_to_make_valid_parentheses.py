"""1249. Minimum Remove to Make Valid Parentheses"""

class Solution:
    """Solution Class"""

    def minRemoveToMakeValid(self, s: str) -> str:
        """
            This function removes the minimum number of parentheses to make a valid string. It keeps track of the index in the string to then replace the parentheses that doesn't have a valid pair. This is done in O(N) time.
        """
        s = list(s)
        opened = []

        for i, char in enumerate(s):
            if char == "(":
                opened.append(i)
            elif char == ")":
                if opened:
                    opened.pop()
                else:
                    s[i] = ""

        while opened:
            s[opened.pop()] = ""

        return "".join(s)
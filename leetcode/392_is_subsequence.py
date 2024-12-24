"""392. Is Subsequence"""
class Solution:
    """Solution Class"""

    def isSubsequence( self, s: str, t: str ) -> bool:
        """
            This function determines if a substring, s, can be created based on the characters found in string, t.
            The order of the characters seen in both strings matter, they have to be in the same sequence.
            This solution leverages this by traversing through string t until all the characters are matched in the
            subsequence or until the end of string t is reached. This ensures a O(n) time complexity where n is the
            length of string t.
        """
        s_pointer, t_pointer = 0, 0

        while t_pointer  < len(t) and s_pointer < len(s):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            t_pointer += 1

        return s_pointer == len(s)
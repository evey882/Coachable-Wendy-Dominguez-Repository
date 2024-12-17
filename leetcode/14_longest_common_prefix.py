"""14. Longest Common Prefix"""

from typing import List

class Solution:
    """Solution Class"""

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
            This function identifies what the longest prefix is based on an array of words passed in.
            Using an empty string to both append and be used in case there is no longest common prefix,
            this function traverses through all the characters of the first word found in the passed array
            and based on this, compares it with the character found in the other strings in that slot. If
            there is a mismatch it will return the result up to whatever is stored there.
        """
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
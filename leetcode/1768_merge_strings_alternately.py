"""1768. Merge Strings Alternately"""

class Solution:
    """Solution Class"""
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        This function goes through the max word and checks in each word if there is a valid character. When there is, it is added to an array to keep the efficiency down. Once both strings are traversed, the array is joined and a string is returned of both words merged alternately.
        """
        merged_string = []
        len1 = len(word1)
        len2 = len(word2)

        for char in range(max( len1, len2 )):
            if char < len1:
                merged_string.append( word1[char] )
            if char < len2:
                merged_string.append( word2[char] )

        return "".join(merged_string)
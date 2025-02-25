"""1331. Rank Transform of An Array"""

class Solution:
    """Solution Class"""
    def arrayRankTransform(self, arr):
        """
        This function takes in an array of integers that needs to be swapped out by their corresponding rank from smallest to largest. It does so by creating a map of the sorted version and mapping the corresponding rank. It then goes over the original array and swaps it out for the correct rank.
        """
        sorted_ver = sorted( set(arr) )

        rank = { num: rank + 1 for rank, num in enumerate(sorted_ver) }

        return [ rank[num] for num in arr ]
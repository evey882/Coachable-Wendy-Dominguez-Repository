"""169. Majority Element"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
            This function returns the number that takes up the majority of spaces in
            the passed array of nums. It does this in O(n) time with O(1) space.
        """
        res, count = 0, 0

        for num in nums:
            if count == 0:
                res = num
            if res == num:
                count += 1
            else:
                count -= 1

        return res
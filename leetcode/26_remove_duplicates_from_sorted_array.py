"""26. Remove Duplicates from Sorted Array"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
            This function traverses the inputted array, keeps a count of the size
            of the array after removing the duplicates and ignores the elements after
            that size of k. It removes these duplicates in-place.
        """
        k = 1

        for idx in range(1, len(nums)):
            if nums[idx] != nums[idx - 1]:
                nums[k] = nums[idx]
                k += 1

        return k
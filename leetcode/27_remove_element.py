"""27. Remove Element"""

from typing import List

class Solution:
    """Solution Class"""

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        This function removes the integers located in the input array that match the inputted
        val. It does this in-place by going through the array in one pass, having a pointer to
        keep track of the length of the remaining elements that don't match val, and moving each
        one to the front via copying.
        """

        k = 0

        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[k] = nums[idx]
                k += 1

        return k
"""1. Two Sum"""

from typing import List

class Solution:
    """Solution Class"""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            This function determines in one pass, where the addends are located for a
            given target. Once they are found, their corresponding index is returned.
            It utilizes the benefits of a hashmap, to hold unique keys and simple mathematical
            logic to identify the second number of the equation to make the function true.
        """

        seen = {}

        for idx in range(len(nums)):
            complement = target - nums[idx]

            if complement in seen:
                return [seen[complement], idx]

            seen[nums[idx]] = idx
class Solution:
    """Solution Class"""
    def moveZeros(self, nums) -> None:
        """
        In this function, an array is passed in that may contain zeros. if it does then they are swapped over by non zero integers, until all the zeros are at the end of the array. This is completed in one pass utilizing only constant variables. 
        """

        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
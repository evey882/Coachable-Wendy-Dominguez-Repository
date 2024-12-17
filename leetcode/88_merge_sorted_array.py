"""88. Merge Sorted Array"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """
        This function merges two ascending order arrays, in-place of the first passed array.
        It begins by going through both arrays at the same time if there are elements in both, otherwise,
        it will go through the nums2 and move them over to nums1 and order the elements in descending order
        starting from the end of nums1.
        """

        if n != 0:
            end_nums1 = len(nums1) - 1

            while m > 0 and n > 0:
                if nums2[ n - 1] >= nums1[ m - 1 ]:
                    nums1[end_nums1] = nums2[ n - 1 ]
                    n -= 1
                else:
                    nums1[ end_nums1 ] = nums1 [ m - 1 ]
                    m -= 1
                end_nums1 -= 1

            while n > 0:
                nums1 [ end_nums1 ] = nums2[ n - 1 ]
                n -= 1
                end_nums1 -= 1
"""1539. Kth Missing Positive Number"""

class Solution:
    """Solution Class"""

    def findKthPositive(self, arr, k) -> int:
        """
        This function utilizes binary search to efficiently determines the kth missing number by using binary search. It calculates how many numbers are missing and then determines where the kth missing number would fall. And finally returns it once it finds it.
        """
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = low + (high - low)
            missing = arr[mid] - (mid + 1)

            if missing < k:
                low = mid + 1
            else:
                high = mid - 1

        return low + k
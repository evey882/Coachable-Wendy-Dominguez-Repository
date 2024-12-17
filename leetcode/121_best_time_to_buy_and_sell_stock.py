"""121. Best Time to Buy and Sell Stock"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
            This function returns the max profit possible from the passed in array, if
            no positive profit is made it returns 0. The space in the array determines
            the day.
        """

        minimum = prices[0]
        max_profit = 0

        for idx in range(1, len(prices)):
            minimum = min(prices[idx], minimum)
            max_profit = max(max_profit, prices[idx] - minimum)

        return max_profit
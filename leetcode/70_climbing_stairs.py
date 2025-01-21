"""70. Climbing Stairs"""
class Solution:
    """Solution Class"""
    def climbStairs(self, n: int) -> int:
        """
        in this solution we use a dynamic programming solution to avoid running into a time limit exceeded.
        This problem takes a form of the fibonacci sequence, and knowing this we are able to determine the base cases and use those to further calculate the rest of the possible steps that can be taken.
        We do this in O(n) with O(1) space.
        """
        base = 0
        base2 = 1

        for i in range(1, n + 1):
            curr = base + base2

            base = base2
            base2 = curr

        return base2
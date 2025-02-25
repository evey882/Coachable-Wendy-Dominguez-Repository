"""339. Nested List Weight Sum"""

from collections import deque

class Solution:
    """Solution Class"""

    def depthSum(self, nestedList) -> int:
        """

        This function takes in a list of integers that can contain a nested list of integers. Based on each level of nested lists we're tasked with multiplying the integers with the level. Thereby getting a sum of the integers times the depth, we are able to complete this using a deque and doing a BFS approach.

        """
        weightedSum = 0
        depth = 1

        queue = deque([( nestedList, depth )])

        while queue:
            currList, currDepth = queue.popleft()
            for elem in currList:
                if elem.isInteger():
                    weightedSum += elem.getInteger() * currDepth
                else:
                    queue.append(( elem.getList(), currDepth + 1 ))
        return weightedSum
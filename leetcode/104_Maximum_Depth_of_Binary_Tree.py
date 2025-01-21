"""104. Maximum Depth of Binary Tree"""

from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Solution Class"""
    def maxDepth (self, root) -> int:
        """
        This approach traverses the tree in a breadth first search, it clears the level of the tree before moving onto the next. It keeps track of the level and only increments them when that level is fully cleared.
        This approach clears the tree in O(n) where n is the total number of nodes and O(m) where m is the max number of nodes in a level.
        """
        if not root: return 0

        level = 0
        queue = deque([root])

        while queue:
            for node in range(len(queue)):
                nde = queue.popleft()
                if nde.left:
                    queue.append(nde.left)
                if nde.right:
                    queue.append(nde.right)

            level += 1

        return level
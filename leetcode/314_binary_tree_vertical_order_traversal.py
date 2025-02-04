"""314. Binary Tree Vertical Order Traversal"""

from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Solution Class"""
    def verticalOrder(self, root):
        """ This solution utilizes a dictionary and queue to visit all the nodes and organize them via columns and keeping it in a left to right order. It does so in a breath first search method, whilst also tracking the corresponding column. The runtime is O(N) and takes up a space of O(N) since each node needs to be visited."""
        if not root: return []

        columns = defaultdict(list)

        queue = deque([( root, 0 )])
        while queue:
            node, colIdx = queue.popleft()
            columns[colIdx].append( node.val )

            if node.left:
                queue.append(( node.left, colIdx - 1 ))

            if node.right:
                queue.append(( node.right, colIdx + 1 ))

        return [columns[colIdx] for colIdx in range( min(columns), max(columns) + 1 )]
"""543. Diameter of Binary Tree"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Solution Class"""
    def diameterOfBinaryTree(self, root):
        """ This function traverses the tree in a DFS manner, to calculate the diameter. It increments the size by one after each node is processed, thus finding the height of each subtree. """
        self.max = 0

        def height(node):
            if not node:
                return 0

            left = height( node.left )
            right = height( node.right )

            self.max = max( left, right ) + 1

        height( root )
        return self.max
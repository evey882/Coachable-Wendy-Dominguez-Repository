"""226. Invert Tree"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution Class"""
    def invertTree(self, root):
        """
        In this function, recursion is used to switch the node pointers of the tree, only when the root is a valid node, swapping it and therefore "inverting" the tree.
        It is then called on the newly swapped nodes to do the process again. If the base case is not met then we return the node after we have swapped its possible children.
        """
        if not root: return

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
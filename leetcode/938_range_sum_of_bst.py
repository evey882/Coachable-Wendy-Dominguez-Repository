"""938. Range Sum of BST"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Solution Class"""
    def rangeSumBST(self, root, low: int, high: int) -> int:
        """
        This function takes advantage that this is a binary tree and so we can leverage this to check only the necessary tree branches that meet the criteria.
        We use recursion on getting the summation of the subtrees, before returning the final sum. At most, this function covers all the nodes in the tree.
        """
        summation = 0

        if root:
            if low <= root.val <= high:
                summation += root.val

            if low <= root.val:
                summation += self.rangeSumBST(root.left, low, high)

            if root.val <= high:
                summation += self.rangeSumBST(root.right, low, high)

        return summation